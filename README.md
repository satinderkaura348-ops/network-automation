# Network Automation

A central repository for network automation tools, scripts, and Ansible playbooks used to improve operational efficiency, consistency, and standardisation across the network environment.

This repository contains automation solutions developed to reduce manual effort, improve deployment quality, and support day-to-day network operations through repeatable and low-risk workflows.

---

## Objectives

- Reduce manual operational tasks
- Improve configuration consistency
- Standardise upgrade and validation procedures
- Increase automation adoption within the Network Engineering team
- Provide reusable tools for common operational activities
- Generate reliable reporting and audit records

---

## Repository Structure

```text
network-automation/
│
├── c9300-precheck/
│   ├── playbooks/
│   ├── roles/
│   ├── group_vars/
│   ├── reports/
│   ├── run_precheck.py
│   ├── generate_inventory.py
│   └── README.md
│
└── README.md
```

Each project contains its own documentation, requirements, and usage instructions.

---

## Current Projects

### Catalyst 9300 Upgrade Precheck Tool

An Ansible-based pre-upgrade validation tool for Cisco Catalyst 9300 switches.

#### Purpose

Performs a series of read-only health checks against Catalyst 9300 switches before IOS-XE upgrade activities.

The tool helps identify devices that may require remediation before an upgrade can be safely performed.

#### Validation Checks

- Catalyst 9300 platform verification
- IOS-XE version collection
- Install mode verification
- Flash storage validation
- Stack member health validation
- Boot variable verification
- Secondary boot path detection
- CPU utilisation checks

#### Generated Reports

```text
reports/
├── all_switches.csv
└── exceptions.csv
```

**all_switches.csv**

Contains results for every switch processed.

**exceptions.csv**

Contains only switches that failed one or more validation checks.

For complete usage instructions, refer to the project README located within the project directory.

---

## Design Principles

The automation solutions within this repository follow the principles below:

- Read-only by default
- Low operational risk
- Repeatable execution
- Simple deployment and maintenance
- Clear reporting and auditing
- Version controlled development
- Modular and reusable design

---

## Security Considerations

- Credentials must never be committed to source control.
- Runtime credentials should be generated dynamically where possible.
- Sensitive files should be excluded using `.gitignore`.
- Follow organisational security policies when handling authentication data and generated reports.

---

## Requirements

Requirements vary by project.

Typical dependencies may include:

- Python 3.x
- Ansible
- Cisco IOS Collection
- SSH connectivity to managed devices

Example:

```bash
ansible-galaxy collection install cisco.ios
```

---

## Contributing

Contributions are encouraged.

Before submitting changes:

1. Test thoroughly in a non-production environment.
2. Update relevant documentation.
3. Follow existing coding and naming conventions.
4. Ensure automation remains safe and predictable.
5. Validate all changes before committing.

---

## Roadmap

Future automation initiatives may include:

- IOS-XE upgrade automation
- Configuration compliance auditing
- Interface health monitoring
- Stack health reporting
- Software lifecycle management
- Inventory and asset reporting
- Dashboard and reporting enhancements

---

## Maintainers

Network Engineering Team

---

## Disclaimer

All automation within this repository should be tested and validated prior to production use.

Users are responsible for ensuring change management, maintenance windows, and operational procedures are followed in accordance with organisational standards.
