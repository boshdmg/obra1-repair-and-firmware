$dfu="$env:APPDATA\Artiphon\Orba\UpdateUtilities\dfu-util-win\dfu-util.exe"
$S="C:\Users\dgarn\AppData\Local\Temp\claude\f1e358193df3bb72\9a5c4984-afc8-4478-9682-a3dd1ff948f5\scratchpad"
function Present { [bool](Get-PnpDevice -PresentOnly -ErrorAction SilentlyContinue | Where-Object InstanceId -match 'VID_0483&PID_DF11') }
function Others { (Get-PnpDevice -PresentOnly -ErrorAction SilentlyContinue | Where-Object { $_.InstanceId -match '^USB' -and $_.InstanceId -notmatch 'VID_047F|VID_045E|VID_17E9|VID_05E3|VID_2357|VID_06C4|ROOT_HUB' } | ForEach-Object { "$($_.Status)|$($_.FriendlyName)|$($_.InstanceId)" }) -join ' ;; ' }
$end=(Get-Date).AddMinutes(30)
if(Present){ "waiting for unplug..."; while(Present){ Start-Sleep -Milliseconds 400 } }
while(-not (Present)){ if((Get-Date) -gt $end){"timed out"; exit}; Start-Sleep -Milliseconds 300 }
"$(Get-Date -f T) bootloader detected; loading immediately"
Start-Sleep -Milliseconds 300
"=== load engine into RAM ==="
& $dfu -a 0 -s "0x20010000:force" -D "$S\re\seg_20010000.bin" 2>&1 | Out-String
if($LASTEXITCODE -ne 0){ "RAM load failed, stopping"; exit }
"=== cue: asking user to press power ==="
Add-Type -AssemblyName System.Speech; $sp=New-Object System.Speech.Synthesis.SpeechSynthesizer
$sp.Speak("Get ready to press the power button.")
Start-Sleep 1; $sp.Speak("Three. Two. One. Press and hold power now.")
Start-Sleep -Milliseconds 700
"=== start firmware (power button should still be held) $(Get-Date -f T) ==="
& $dfu -a 0 -s "0x08000000:force:leave" -D "$S\re\empty.bin" 2>&1 | Out-String
Start-Sleep -Milliseconds 1500; $sp.SpeakAsync("Let go now.") | Out-Null; $last=''; $t0=Get-Date
while(((Get-Date)-$t0).TotalSeconds -lt 90){ $o=Others; if($o -ne $last){ "$([int]((Get-Date)-$t0).TotalSeconds)s -> [$o]"; $last=$o }; Start-Sleep -Milliseconds 300 }
"done watching"



