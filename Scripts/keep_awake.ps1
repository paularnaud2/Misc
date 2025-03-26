$wsh = New-Object -ComObject WScript.Shell

# Infinite loop to keep system awake
while ($true) {
    # Simulate a harmless key press (F15 key which typically does nothing)
    $wsh.SendKeys('{F15}')
    
    # Wait for 1 minute before next key press
    Start-Sleep -Seconds 30
    
    # Optional: Display status in console
    Write-Host "System kept awake at $(Get-Date -Format 'HH:mm:ss')"
}
