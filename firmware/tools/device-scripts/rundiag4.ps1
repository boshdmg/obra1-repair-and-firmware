$dfu="$env:APPDATA\Artiphon\Orba\UpdateUtilities\dfu-util-win\dfu-util.exe"
$S="C:\Users\dgarn\AppData\Local\Temp\claude\f1e358193df3bb72\9a5c4984-afc8-4478-9682-a3dd1ff948f5\scratchpad"
function Present { [bool](Get-PnpDevice -PresentOnly -ErrorAction SilentlyContinue | Where-Object InstanceId -match 'VID_0483&PID_DF11') }
function GoodRes { $found=$false
  foreach($addr in '0x2003F000','0x20020800'){ $f="$S\diag\result_$addr.bin"; Remove-Item $f -ErrorAction SilentlyContinue
    & $dfu -a 0 -s "$($addr):256:force" -U $f 2>&1 | Out-Null
    if((Test-Path $f) -and (Get-Item $f).Length -eq 256){ $b=[IO.File]::ReadAllBytes($f); $m=[BitConverter]::ToUInt32($b,0)
      Write-Host ("read {0} magic=0x{1:X8}" -f $addr,$m); if($m -eq [uint32]3517317121){ $found=$true } } }
  return $found }
$end=(Get-Date).AddMinutes(30)
if(Present){ "waiting for the Orba to be unplugged first..."; while(Present){ if((Get-Date) -gt $end){"timed out"; exit}; Start-Sleep -Milliseconds 400 } }
"unplugged; waiting for fresh plug-in"
while(-not (Present)){ if((Get-Date) -gt $end){"timed out"; exit}; Start-Sleep -Milliseconds 300 }
"$(Get-Date -f T) bootloader detected - running diagnostic now"
Start-Sleep -Milliseconds 800
& $dfu -a 0 -s "0x20020000:force:leave" -D "$S\diag\diag_stub.bin" 2>&1 | Select-String 'successfully|rror' | Out-String
$t=0; Start-Sleep 2; while(-not (Present) -and $t -lt 60){ Start-Sleep 1; $t++ }
"bootloader back: $(Present) after ~$($t+2)s"
if(Present){ Start-Sleep 1; $r=GoodRes; if($r){"RESULTS FOUND"} else {"no results"} }
