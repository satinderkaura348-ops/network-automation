#!/usr/bin/env python3

import json

inventory = {
    "_meta": {
        "hostvars": {}
    },
    "upgrade_candidates": {
        "hosts": []
    }
}

with open("switches.txt") as f:
    for line in f:
        ip = line.strip()

        if not ip:
            continue

        inventory["upgrade_candidates"]["hosts"].append(ip)

        inventory["_meta"]["hostvars"][ip] = {
            "ansible_host": ip
        }

print(json.dumps(inventory))
