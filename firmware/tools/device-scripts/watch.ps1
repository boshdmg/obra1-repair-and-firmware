$base = (Get-PnpDevice -PresentOnly).InstanceId
$vols = (Get-Volume).UniqueId
$end = (Get-Date).AddMinutes(4)
while ((Get-Date) -lt $end) {
  Start-Sleep -Seconds 2
  $now = Get-PnpDevice -PresentOnly
  $new = $now | Where-Object { $base -notcontains $_.InstanceId }
  foreach ($d in $new) { "{0} NEW  {1} | {2} | {3} | {4}" -f (Get-Date -f T), $d.Status, $d.Class, $d.FriendlyName, $d.InstanceId; $base += $d.InstanceId }
  $gone = $base | Where-Object { ($now.InstanceId) -notcontains $_ }
  foreach ($g in $gone) { "{0} GONE {1}" -f (Get-Date -f T), $g; $base = $base | Where-Object { $_ -ne $g } }
  Get-Volume | Where-Object { $vols -notcontains $_.UniqueId } | ForEach-Object { "{0} VOLUME {1}: label='{2}' fs={3} size={4}" -f (Get-Date -f T), $_.DriveLetter, $_.FileSystemLabel, $_.FileSystem, $_.Size; $vols += $_.UniqueId }
}
"done"
