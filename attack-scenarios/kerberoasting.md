# Kerberoasting Attack Scenario

## Description
Kerberoasting is a technique used to extract service account credential hashes from Active Directory.

## Execution
1. The attacker uses a tool like `Invoke-Kerberoast` or `Impacket` to request service tickets (TGS) for accounts with Service Principal Names (SPNs).
2. The tickets are extracted and saved for offline cracking.

## Detection
- **Event ID**: 4769 (A Kerberos service ticket was requested)
- **Indicators**: Ticket Options `0x40810000`, Ticket Encryption Type `0x17` (RC4).
- **Wazuh Rule**: `100001`
