# Lab Setup Guide

This guide covers the prerequisites, installation, and configuration steps to reproduce the Wazuh SIEM Detection Lab.

## Prerequisites

- A host machine with at least **16 GB RAM** and **200 GB free disk space**
- [VirtualBox](https://www.virtualbox.org/) installed
- ISO images for:
  - Windows Server 2022
  - Windows 11 Pro
  - Ubuntu Server 22.04 LTS
  - Kali Linux
  - pfSense CE

## Network Configuration

All VMs are connected to a **Host-only** or **Internal** VirtualBox network on the `192.0.2.0/24` subnet.

| VM | IP Address | Role |
|---|---|---|
| pfSense | 192.0.2.1 | Gateway / Firewall |
| Windows Server 2022 | 192.0.2.10 | Domain Controller (lab.local) |
| Windows 11 | 192.0.2.20 | Workstation / Wazuh Agent |
| Kali Linux | 192.0.2.30 | Attacker Machine |
| SIEM01 (Wazuh SIEM) | 192.0.2.40 | SIEM Server |

## Wazuh Server Installation (Ubuntu 22.04)

```bash
# Download and run the Wazuh installation assistant
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh
sudo bash wazuh-install.sh -a
```

After installation, the Wazuh dashboard is accessible at `https://192.0.2.40`.

## Wazuh Agent Deployment (Windows)

Run the following in an elevated PowerShell session on the Windows endpoint:

```powershell
Invoke-WebRequest -Uri "https://packages.wazuh.com/4.x/windows/wazuh-agent-4.7.0-1.msi" -OutFile "wazuh-agent.msi"
Start-Process -FilePath "msiexec.exe" -ArgumentList '/i wazuh-agent.msi /q WAZUH_MANAGER="192.0.2.40" WAZUH_REGISTRATION_SERVER="192.0.2.40"' -Wait
NET START WazuhSvc
```

## Sysmon Installation

Deploy Sysmon on the Windows endpoint for enhanced process and network telemetry:

```powershell
# Download Sysmon
Invoke-WebRequest -Uri "https://download.sysinternals.com/files/Sysmon.zip" -OutFile "Sysmon.zip"
Expand-Archive Sysmon.zip -DestinationPath Sysmon
cd Sysmon
.\Sysmon64.exe -accepteula -i ..\sysmon\sysmon-config.xml
```

## Custom Wazuh Rules

Copy the custom rules from `wazuh/rules/` to the Wazuh manager:

```bash
sudo cp wazuh/rules/*.xml /var/ossec/etc/rules/
sudo systemctl restart wazuh-manager
```

## pfSense Firewall Rules

Import the rules documented in [pfsense/firewall-rules.md](../pfsense/firewall-rules.md) via the pfSense web interface under **Firewall > Rules**.

## Verification

After setup, verify the environment by running a test detection:

1. On the Kali machine, run: `nmap -sV 192.0.2.10`
2. Check the Wazuh dashboard for alerts under the **Security Events** module.
3. Confirm that network discovery alerts (T1046) are triggered.
