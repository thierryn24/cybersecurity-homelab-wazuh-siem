# Lateral Movement Scenario

## Description
After compromising an initial endpoint, the attacker moves laterally to other systems in the network, often targeting the Domain Controller.

## Execution
1. The attacker uses compromised credentials or pass-the-hash techniques.
2. Tools like `CrackMapExec` or `PsExec` are used to authenticate to other machines via SMB or WinRM.

## Detection
- **Event ID**: 4624 (Successful Logon)
- **Indicators**: Logon Type 3 (Network), Authentication Package `NTLM`.
- **Wazuh Rule**: `100003`
