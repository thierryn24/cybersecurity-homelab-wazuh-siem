# Lab Architecture

The lab environment consists of five virtual machines hosted in VirtualBox, interconnected on an isolated internal network segment (`10.10.10.0/24`) replicating a small corporate Active Directory environment.

## Network Diagram

```text
10.10.10.0/24 — Isolated Internal Network
├── Windows Server 2022 (Domain Controller)   10.10.10.10
├── Windows 11 Workstation                    10.10.10.20
├── Kali Linux (Attacker)                     10.10.10.30
├── Ubuntu — Wazuh SIEM Server                10.10.10.40
└── pfSense Firewall                          10.10.10.1
```

## Components

1. **Domain Controller (Windows Server 2022)**: Hosts the Active Directory domain `corp.local`.
2. **Workstation (Windows 11)**: Represents a typical user endpoint.
3. **Attacker Machine (Kali Linux)**: Used to execute simulated attacks.
4. **SIEM Server (Ubuntu + Wazuh)**: Centralized log aggregation and analysis.
5. **Firewall (pfSense)**: Manages internal network traffic and enforces security rules.
