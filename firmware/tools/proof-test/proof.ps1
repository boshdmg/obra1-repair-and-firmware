$dfu="$env:APPDATA\Artiphon\Orba\UpdateUtilities\dfu-util-win\dfu-util.exe"
$P="C:\Users\dgarn\AppData\Local\Temp\claude\f1e358193df3bb72\9a5c4984-afc8-4478-9682-a3dd1ff948f5\scratchpad\proof"
$E="C:\Users\dgarn\AppData\Local\Temp\claude\f1e358193df3bb72\9a5c4984-afc8-4478-9682-a3dd1ff948f5\scratchpad\re\empty.bin"
function Present { [bool](Get-PnpDevice -PresentOnly -ErrorAction SilentlyContinue | Where-Object InstanceId -match 'VID_0483&PID_DF11') }
function T { (Get-Date).ToString('HH:mm:ss.fff') }
function Dfu([string[]]$a){ $o = & $dfu @a 2>&1 | Out-String; $script:rc=$LASTEXITCODE; return $o }
$end=(Get-Date).AddMinutes(30)
if(Present){ "$(T) waiting for unplug..."; while(Present){ Start-Sleep -Milliseconds 300 } }
while(-not (Present)){ if((Get-Date) -gt $end){"timed out"; exit}; Start-Sleep -Milliseconds 200 }
"$(T) STEP 0: bootloader detected"
Start-Sleep -Milliseconds 300
$o=Dfu @('-a','0','-s','0x20020000:force','-D',"$P\proof.bin"); "$(T) STEP 1: write program to RAM -> exit $rc " + (($o -split "`n" | Select-String 'successfully|rror|No DFU') -join ' ')
if($rc -ne 0){ "STOP: write failed"; exit }
Remove-Item "$P\readback.bin" -ErrorAction SilentlyContinue
$o=Dfu @('-a','0','-s','0x20020000:512:force','-U',"$P\readback.bin"); "$(T) STEP 2: read back -> exit $rc"
if(Test-Path "$P\readback.bin"){ $a=[IO.File]::ReadAllBytes("$P\proof.bin"); $b=[IO.File]::ReadAllBytes("$P\readback.bin"); $d=0; for($i=0;$i -lt 512;$i++){ if($a[$i] -ne $b[$i]){$d++} }; "        read $($b.Length) bytes, differing from what was written: $d" } else { "STOP: readback failed"; exit }
$o=Dfu @('-a','0','-s','0x20020000:force:leave','-D',$E); "$(T) STEP 3: run program -> exit $rc " + (($o -split "`n" | Select-String 'successfully|rror|MANIFEST') -join ' ')
$gone=$false; $t0=Get-Date
while(((Get-Date)-$t0).TotalSeconds -lt 20){ $p=Present; if(-not $p -and -not $gone){ $gone=$true; "$(T) STEP 4: bootloader disconnected" }; if($p -and $gone){ "$(T) STEP 4: bootloader came back"; break }; Start-Sleep -Milliseconds 100 }
if(-not $gone){ "$(T) STEP 4: bootloader never disconnected (Windows may not have noticed)" }
if(-not (Present)){ "$(T) RESULT: bootloader not present after 20s -> no proof of execution"; exit }
Start-Sleep -Milliseconds 500
Remove-Item "$P\result.bin" -ErrorAction SilentlyContinue
$o=Dfu @('-a','0','-s','0x20020100:16:force','-U',"$P\result.bin"); "$(T) STEP 5: read result -> exit $rc"
if(Test-Path "$P\result.bin"){ $r=[IO.File]::ReadAllBytes("$P\result.bin"); "        CPUID=0x{0:X8}  MARKER=0x{1:X8}  RCC_CSR=0x{2:X8}" -f [BitConverter]::ToUInt32($r,0),[BitConverter]::ToUInt32($r,4),[BitConverter]::ToUInt32($r,8) }
