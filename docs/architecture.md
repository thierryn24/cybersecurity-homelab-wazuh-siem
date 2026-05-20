# Lab Architecture

The lab environment consists of five virtual machines hosted in VirtualBox, interconnected on an isolated internal network segment (`192.0.2.0/24`) replicating a small corporate Active Directory environment.

## Network Diagram

```text
192.0.2.0/24 — Isolated Internal Network
├── DC01 (Domain Controller)   192.0.2.10
├── WKS01 (Workstation)                    192.0.2.20
├── KALI01 (Attacker)                     192.0.2.30
├── SIEM01 — Wazuh SIEM Server                192.0.2.40
└── pfSense Firewall                          192.0.2.1
```

## Components

1. **Domain Controller (Windows Server 2022)**: Hosts the Active Directory domain `lab.local`.
2. **Workstation (Windows 11)**: Represents a typical user endpoint.
3. **Attacker Machine (Kali Linux)**: Used to execute simulated attacks.
4. **SIEM Server (Ubuntu + Wazuh)**: Centralized log aggregation and analysis.
5. **Firewall (pfSense)**: Manages internal network traffic and enforces security rules.
