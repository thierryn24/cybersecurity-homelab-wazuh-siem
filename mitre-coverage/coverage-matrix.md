# MITRE ATT&CK Coverage Matrix

## Coverage Summary

| Tactic | Techniques Tested | Detected | Coverage |
|--------|-------------------|----------|----------|
| Credential Access | 6 | 5 | 83% |
| Lateral Movement | 4 | 4 | 100% |
| Defense Evasion | 5 | 3 | 60% |
| Discovery | 3 | 3 | 100% |
| Exfiltration | 3 | 2 | 67% |

## Detailed Technique Mapping

| Tactic | Technique ID | Technique Name | Detection Rule | Status |
|--------|---|---|---|---|
| Credential Access | T1558.003 | Kerberoasting | 100001 | Detected |
| Credential Access | T1003.001 | OS Credential Dumping: LSASS Memory | 100002 | Detected |
| Credential Access | T1557.001 | LLMNR/NBT-NS Poisoning and SMB Relay | Built-in | Detected |
| Credential Access | T1110 | Brute Force | Built-in | Detected |
| Credential Access | T1110.001 | Password Guessing | Built-in | Detected |
| Credential Access | T1110.003 | Password Spraying | Built-in | Not Detected |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | 100003 | Detected |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | Built-in | Detected |
| Lateral Movement | T1550.002 | Pass the Hash | Built-in | Detected |
| Lateral Movement | T1570 | Lateral Tool Transfer | Built-in | Detected |
| Defense Evasion | T1562.001 | Disable or Modify Tools | Built-in | Detected |
| Defense Evasion | T1070.001 | Clear Windows Event Logs | Built-in | Detected |
| Defense Evasion | T1036 | Masquerading | Built-in | Detected |
| Defense Evasion | T1027 | Obfuscated Files or Information | Built-in | Not Detected |
| Defense Evasion | T1218 | System Binary Proxy Execution | Built-in | Not Detected |
| Discovery | T1046 | Network Service Discovery | Built-in | Detected |
| Discovery | T1135 | Network Share Discovery | Built-in | Detected |
| Discovery | T1087 | Account Discovery | Built-in | Detected |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | Built-in | Detected |
| Exfiltration | T1048 | Exfiltration Over Alternative Protocol | Built-in | Detected |
| Exfiltration | T1567 | Exfiltration Over Web Service | Built-in | Not Detected |
