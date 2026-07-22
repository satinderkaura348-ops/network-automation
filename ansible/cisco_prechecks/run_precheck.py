from getpass import getpass
from pathlib import Path
import subprocess
import time
import os

BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

reports = Path("reports")

reports.mkdir(exist_ok=True)

(reports / "all_switches.csv").write_text(
    "Hostname,IP,Platform,Version,BootVariable,CPUPercent,FreeSpaceBytes,Status\n"
)
(reports / "exceptions.csv").write_text(
    "Hostname,IP,Status,Reason\n"
)
(reports / "progress.txt").write_text("")

print("\n================================")
print("Catalyst Precheck Tool")
print("================================\n")

username = input("Username: ")
password = getpass("Password: ")

vault_content = f"""vault_ansible_user: {username}
vault_ansible_password: {password}
"""

Path("group_vars/vault.yml").write_text(vault_content)

print("\nRunning prechecks...\n")

switch_count = len(
    [
        line
        for line in Path("switches.txt").read_text().splitlines()
        if line.strip()
    ]
)

print(f"Switches Loaded: {switch_count}\n")

process = subprocess.Popen(
    [
        "ansible-playbook",
        "-i",
        "generate_inventory.py",
        "playbooks/precheck.yml"
    ],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

while process.poll() is None:

    try:
        completed = len(
            [
                line
                for line in (reports / "progress.txt")
                .read_text()
                .splitlines()
                if line.strip()
            ]
        )
    except:
        completed = 0

    percent = (
        int((completed / switch_count) * 100)
        if switch_count
        else 0
    )

    bar_length = 30

    filled = int(
        bar_length * completed / switch_count
    ) if switch_count else 0

    bar = (
        "█" * filled +
        "-" * (bar_length - filled)
    )

    print(
        f"\r[{bar}] {completed}/{switch_count} ({percent}%)",
        end="",
        flush=True
    )

    time.sleep(0.2)

process.wait()

try:
    completed = len(
        [
            line
            for line in (reports / "progress.txt")
            .read_text()
            .splitlines()
            if line.strip()
        ]
    )
except:
    completed = 0

print(
    f"\r[{'█' * 30}] {completed}/{switch_count} (100%)"
)
print("\n")

if process.returncode == 0:
    print("✅ Prechecks completed successfully.\n")
    print("Reports generated:")
    print("  reports/all_switches.csv")
    print("  reports/exceptions.csv")
else:
    print("❌ Prechecks failed.")


vault_file = Path("group_vars/vault.yml")

try:
    vault_file.unlink()
except FileNotFoundError:
    pass
