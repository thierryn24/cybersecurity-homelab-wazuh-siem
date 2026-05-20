#!/usr/bin/env python3
"""
Alert Enrichment Script
Enriches Wazuh alerts with threat intelligence data.

Configuration via environment variables:
  WAZUH_MANAGER_IP   - IP address of the Wazuh manager
  TI_API_KEY         - Threat intelligence API key (required for live lookups)
  TI_API_URL         - Threat intelligence API endpoint
"""

import json
import os
import sys

# Configuration — loaded from environment variables, never hardcoded
WAZUH_MANAGER_IP = os.environ.get("WAZUH_MANAGER_IP", "192.0.2.40")
TI_API_KEY = os.environ.get("TI_API_KEY", "")
TI_API_URL = os.environ.get("TI_API_URL", "https://api.threatintel.example.com/v1/lookup")


def enrich_alert(alert_data: dict) -> dict:
    """Add threat intelligence context to a Wazuh alert."""
    alert_data["enriched"] = True
    alert_data["enrichment_source"] = TI_API_URL

    # Add MITRE ATT&CK context based on rule ID
    rule_id = alert_data.get("rule", {}).get("id", "")
    mitre_map = {
        "100001": {"technique": "T1558.003", "tactic": "Credential Access", "name": "Kerberoasting"},
        "100002": {"technique": "T1003.001", "tactic": "Credential Access", "name": "LSASS Memory Dump"},
        "100003": {"technique": "T1021.002", "tactic": "Lateral Movement", "name": "SMB/Windows Admin Shares"},
    }
    if rule_id in mitre_map:
        alert_data["mitre"] = mitre_map[rule_id]

    return alert_data


if __name__ == "__main__":
    if not TI_API_KEY:
        print("[WARNING] TI_API_KEY not set. Set via: export TI_API_KEY='your-key'", file=sys.stderr)

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            alert = json.load(f)
        enriched = enrich_alert(alert)
        print(json.dumps(enriched, indent=2))
    else:
        print("Usage: alert-enrichment.py <alert.json>")
        print("Environment variables: WAZUH_MANAGER_IP, TI_API_KEY, TI_API_URL")
