# Wazuh SIEM Detection Lab
> Enterprise security monitoring lab with custom detection rules mapped to MITRE ATT&CK

![Wazuh](https://img.shields.io/badge/Wazuh-4.x-blue)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-red)
![Status](https://img.shields.io/badge/Status-Active-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

A production-grade home lab simulating an enterprise environment to develop,
test, and refine detection capabilities. Built to demonstrate practical
SOC engineering skills: from log collection to alert tuning.

This project was developed as a **Final Year Capstone** at Gokstad Akademiet (2026),
co-authored by **Thierry Nimubona** and **Abdou Karim Secka**, under the supervision
of Mazaher Kianpour.

## Architecture

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Hypervisor | VirtualBox | VM hosting with isolated internal network |
| Domain Controller | Windows Server 2022 | AD DS, DNS, GPO |
| Endpoint | Windows 11 Pro | Sysmon + Wazuh agent |
| SIEM | Wazuh 4.x | Log aggregation, alerting |
| Firewall | pfSense CE | Network segmentation, firewall rules |
| Attack Box | Kali Linux | Red team simulation |

**Network segment:** `10.10.10.0/24` — fully isolated from production networks.

See [docs/architecture.md](docs/architecture.md) for the full network diagram and component breakdown.

## Detection Coverage

| Tactic | Techniques Tested | Detected | Coverage |
|--------|-------------------|----------|----------|
| Credential Access | 6 | 5 | 83% |
| Lateral Movement | 4 | 4 | 100% |
| Defense Evasion | 5 | 3 | 60% |
| Discovery | 3 | 3 | 100% |
| Exfiltration | 3 | 2 | 67% |

See [full coverage matrix](mitre-coverage/coverage-matrix.md).

## Featured Detections

- [Kerberoasting (T1558.003)](attack-scenarios/kerberoasting.md)
- [LSASS Dumping (T1003.001)](attack-scenarios/lsass-dump.md)
- [Lateral Movement via SMB/PsExec (T1021.002)](attack-scenarios/lateral-movement.md)

## Custom Wazuh Rules

35+ custom rules mapped to MITRE ATT&CK. See [wazuh/rules/](wazuh/rules/).

Example — LSASS memory dump detection:

```xml
<rule id="100201" level="14">
  <if_sid>60103</if_sid>
  <field name="win.eventdata.targetFilename" type="pcre2">(?i)\\lsass\.dmp</field>
  <description>Possible LSASS memory dump detected</description>
  <mitre>
    <id>T1003.001</id>
  </mitre>
</rule>
```

## Key Results

| Metric | Result |
|---|---|
| Security Events Generated | 15,000+ |
| CVEs Identified | 50 unpatched |
| High Severity CVEs | 38 |
| pfSense Firewall Rules Implemented | 6 |
| MITRE ATT&CK Tactics Covered | Discovery, Credential Access, Defense Evasion |

## Getting Started

Prerequisites, setup, and deployment instructions in [docs/setup.md](docs/setup.md).

## Roadmap

- [ ] Integrate Shuffle SOAR for automated response
- [ ] Add honeypot tier (Cowrie)
- [ ] Simulate full ransomware kill chain
- [ ] Migrate to Elastic Stack for comparison

## Author

**Thierry Nimubona** — Cybersecurity Professional  
🌐 [thierryinfosec.com](https://thierryinfosec.com)  
💼 [LinkedIn](https://linkedin.com/in/thierry-nimubona)

## License

MIT — see [LICENSE](LICENSE)
