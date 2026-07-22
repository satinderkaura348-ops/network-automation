# Catalyst 9300 Precheck Tool

## Purpose

The Catalyst 9300 Precheck Tool is an Ansible-based automation solution designed to validate Cisco Catalyst 9300 switch readiness prior to IOS-XE upgrade activities.

The tool performs a series of read-only health and compliance checks against one or more switches and generates reports identifying devices that may require remediation before an upgrade can proceed.

No configuration changes are made to the switches. The tool only executes operational "show" commands and collects information for analysis.

---

## Checks Performed

The tool validates the following:

- Catalyst 9300 platform verification
- IOS-XE running version
- Install mode verification
- Available flash storage capacity
- Stack member health
- Boot variable configuration
- Secondary boot path detection
- CPU utilisation threshold validation

---

## Reports Generated

### all_switches.csv

Contains the results for every switch processed.

Example:

```csv
Hostname,IP,Platform,Version,BootVariable,CPUPercent,FreeSpaceBytes,Status
