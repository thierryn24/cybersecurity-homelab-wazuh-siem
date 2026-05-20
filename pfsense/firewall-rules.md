# pfSense Firewall Rules

The following rules were implemented to mitigate the simulated attacks:

1. **Block SMB from Attacker Subnet**: Deny TCP port 445 from `10.10.10.30` to any internal IP.
2. **Block RDP from Attacker Subnet**: Deny TCP port 3389 from `10.10.10.30` to any internal IP.
3. **Disable LLMNR**: Block UDP port 5355 across the internal network.
4. **Disable NBT-NS**: Block UDP ports 137, 138, 139 across the internal network.
5. **Block Lateral Movement Paths**: Restrict workstation-to-workstation communication.
6. **Enforce Network Segmentation**: Isolate the attacker machine from the domain controller except for specific required services.
