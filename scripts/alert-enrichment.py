#!/usr/bin/env python3
# Placeholder script for alert enrichment
import json
import sys

def enrich_alert(alert_data):
    # Add threat intelligence data to the alert
    alert_data['enriched'] = True
    alert_data['threat_intel'] = "Sample threat intel data"
    return alert_data

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            alert = json.load(f)
            enriched_alert = enrich_alert(alert)
            print(json.dumps(enriched_alert, indent=2))
    else:
        print("Usage: alert-enrichment.py <alert.json>")
