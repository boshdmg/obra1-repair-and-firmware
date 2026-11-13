$dfu="$env:APPDATA\Artiphon\Orba\UpdateUtilities\dfu-util-win\dfu-util.exe"
$S="C:\Users\dgarn\AppData\Local\Temp\claude\f1e358193df3bb72\9a5c4984-afc8-4478-9682-a3dd1ff948f5\scratchpad"
$end=(Get-Date).AddMinutes(30); $last=''
while((Get-Date) -lt $end){
  $d=Get-PnpDevice -PresentOnly -ErrorAction SilentlyContinue | Where-Object { $_.InstanceId -match '^USB' -and $_.InstanceId -notmatch 'VID_047F|VID_045E|VID_17E9|VID_05E3|VID_2357|VID_06C4|ROOT_HUB' }
  $now=($d | ForEach-Object { "$($_.FriendlyName)|$($_.InstanceId)" }) -join ' ;; '
  if($now -ne $last){ "$(Get-Date -f T) -> [$now]"; $last=$now
    if($now -match 'DF11'){ Remove-Item "$S\ob_now.bin" -ErrorAction SilentlyContinue; & $dfu -a 1 -s 0x1FFF0000:48 -U "$S\ob_now.bin" 2>&1 | Out-Null
      if(Test-Path "$S\ob_now.bin"){ "option bytes now: " + ([BitConverter]::ToString([IO.File]::ReadAllBytes("$S\ob_now.bin")) -replace '-','').ToLower(); exit } } }
  Start-Sleep -Milliseconds 250 }
