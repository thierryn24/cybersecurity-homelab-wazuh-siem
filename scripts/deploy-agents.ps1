# Wazuh Agent Deployment Script
# Usage: .\deploy-agents.ps1 -WazuhManagerIP <IP> -AgentVersion <version>
# 
# Set WAZUH_MANAGER_IP as an environment variable or pass as parameter.
# Never hardcode IP addresses or credentials in scripts.

param(
    [string]$WazuhManagerIP = $env:WAZUH_MANAGER_IP,
    [string]$AgentVersion = "4.7.0"
)

if (-not $WazuhManagerIP) {
    Write-Error "WAZUH_MANAGER_IP not set. Pass -WazuhManagerIP or set environment variable."
    exit 1
}

Write-Host "Deploying Wazuh Agent v$AgentVersion -> Manager: $WazuhManagerIP"

$InstallerUrl = "https://packages.wazuh.com/4.x/windows/wazuh-agent-$AgentVersion-1.msi"
$InstallerPath = "$env:TEMP\wazuh-agent.msi"

Invoke-WebRequest -Uri $InstallerUrl -OutFile $InstallerPath
Start-Process -FilePath "msiexec.exe" `
    -ArgumentList "/i `"$InstallerPath`" /q WAZUH_MANAGER=`"$WazuhManagerIP`" WAZUH_REGISTRATION_SERVER=`"$WazuhManagerIP`"" `
    -Wait

NET START WazuhSvc
Write-Host "Deployment complete. Agent registered to $WazuhManagerIP"
