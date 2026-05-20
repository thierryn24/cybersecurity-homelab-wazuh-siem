# LSASS Memory Dump Scenario

## Description
Attackers dump the memory of the Local Security Authority Subsystem Service (LSASS) to extract plaintext credentials and hashes.

## Execution
1. The attacker gains administrative privileges.
2. Tools like `Mimikatz`, `Procdump`, or Task Manager are used to create a dump file of `lsass.exe`.

## Detection
- **Event ID**: Sysmon Event ID 10 (Process Access)
- **Indicators**: Target Image `lsass.exe`, Granted Access `0x1010`, `0x1410`, or `0x143a`.
- **Wazuh Rule**: `100002`
