$end=(Get-Date).AddMinutes(20); $seen=$false
while((Get-Date) -lt $end){
  $d=Get-PnpDevice -PresentOnly -ErrorAction SilentlyContinue | Where-Object { $_.InstanceId -match '^USB' -and $_.InstanceId -notmatch 'VID_047F|VID_045E|VID_17E9|VID_05E3|VID_2357|VID_06C4|ROOT_HUB' }
  $now=($d | ForEach-Object { "$($_.FriendlyName)|$($_.InstanceId)" }) -join ' ;; '
  if($now -ne $last){ "$(Get-Date -f T) -> [$now]"; $last=$now }
  Start-Sleep -Milliseconds 300
}
