# Cybersecurity Homelab: Cyberattack Simulation & SIEM Detection with Wazuh

**Final Year Capstone Project — Gokstad Akademiet, 2026**  
**Authors:** Thierry Nimubona & Abdou Karim Secka  
**Supervisor:** Mazaher Kianpour

---

## Abstract

This project presents the design, implementation, and evaluation of a virtualized enterprise security monitoring environment built to simulate realistic cyberattack scenarios and assess the detection capabilities of the open-source **Wazuh SIEM** platform.

The lab environment consisted of five virtual machines hosted in VirtualBox:
- Windows Server 2022 Domain Controller
- Windows 11 Workstation
- Kali Linux Attacker Machine
- Wazuh Management Server (Ubuntu)
- pfSense Firewall

All machines were interconnected on an isolated internal network segment (`10.10.10.0/24`) replicating a small corporate Active Directory environment.

---

## Key Results

| Metric | Result |
|---|---|
| Security Events Generated | 15,000+ |
| CVEs Identified | 50 unpatched |
| High Severity CVEs | 38 |
| pfSense Firewall Rules Implemented | 6 |
| MITRE ATT&CK Tactics Covered | Discovery, Credential Access, Defense Evasion |

---

## Attack Scenarios (MITRE ATT&CK Mapped)

| # | Technique | Description |
|---|---|---|
| 1 | T1046 — Network Service Discovery | Network reconnaissance with Nmap |
| 2 | T1135 — Network Share Discovery | Unauthenticated SMB enumeration |
| 3 | T1557.001 — LLMNR/NBT-NS Poisoning | Credential theft via Responder |
| 4 | T1110 — Brute Force | Authentication brute force attacks |

---

## Lab Architecture

```
10.10.10.0/24 — Isolated Internal Network
├── Windows Server 2022 (Domain Controller)   10.10.10.10
├── Windows 11 Workstation                    10.10.10.20
├── Kali Linux (Attacker)                     10.10.10.30
├── Ubuntu — Wazuh SIEM Server                10.10.10.40
└── pfSense Firewall                          10.10.10.1
```

---

## Tools & Technologies

![Wazuh](https://img.shields.io/badge/Wazuh-SIEM-blue)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red)
![Kali Linux](https://img.shields.io/badge/Kali-Linux-557C94)
![pfSense](https://img.shields.io/badge/pfSense-Firewall-darkblue)
![VirtualBox](https://img.shields.io/badge/VirtualBox-Lab-orange)
![Windows Server](https://img.shields.io/badge/Windows_Server-2022-0078D6)

- **SIEM:** Wazuh (open-source)
- **Attacker Tools:** Nmap, Responder, Hydra, CrackMapExec
- **Firewall:** pfSense
- **Virtualization:** VirtualBox
- **Domain:** Windows Active Directory (corp.local)

---

## Project Documents

- [`Cybersecurity Program project Karim & Thierry.docx`](./Cybersecurity%20Program%20project%20Karim%20%26%20Thierry.docx) — Full project report
- [`Lab_Configuration_Guide.docx`](./Lab_Configuration_Guide.docx) — Lab setup and configuration guide
- [`/screenshots`](./screenshots/) — 33 lab screenshots documenting attack execution and Wazuh detections

---

## NICE Framework

- **Work Role:** Defensive Cybersecurity (PD-WRL-001)
- **Category:** Protection and Defense (PD)
- **Key Competencies:** Network protocol analysis, security event analysis, IOC identification, detection rule creation, threat knowledge

---

## Remediation Implemented

Six pfSense firewall rules were deployed as concrete remediations:
1. Block SMB traffic from attacker subnet
2. Block RDP access from attacker subnet
3. Disable LLMNR traffic
4. Disable NBT-NS traffic
5. Block lateral movement paths
6. Enforce network segmentation between attacker and domain

All rules were verified through post-implementation testing — confirmed blocked.

---

## Portfolio

View the full interactive project writeup at: **[thierryinfosec.com/final-year-project](https://thierryinfosec.com/final-year-project)**

---

*Submitted as part of the Cybersecurity Program at Gokstad Akademiet, April 2026.*
