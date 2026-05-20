# Placeholder script for deploying Wazuh agents
$WazuhManagerIP = "10.10.10.40"
$AgentVersion = "4.7.0"

Write-Host "Deploying Wazuh Agent v$AgentVersion to connect to $WazuhManagerIP..."
# Invoke-WebRequest -Uri "https://packages.wazuh.com/4.x/windows/wazuh-agent-$AgentVersion-1.msi" -OutFile "wazuh-agent.msi"
# Start-Process -FilePath "msiexec.exe" -ArgumentList "/i wazuh-agent.msi /q WAZUH_MANAGER='$WazuhManagerIP' WAZUH_REGISTRATION_SERVER='$WazuhManagerIP'" -Wait
Write-Host "Deployment complete."
