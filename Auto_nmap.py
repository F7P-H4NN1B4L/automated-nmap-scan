import subprocess
import re
import shutil
import json
from datetime import datetime
from colorama import Fore, Style, init


BANNER = ("\033[91m" + r"""
FFFFFFFFFFFFFFFFFFFFFFTTTTTTTTTTTTTTTTTTTTTTTPPPPPPPPPPPPPPPPP   
F::::::::::::::::::::FT:::::::::::::::::::::TP::::::::::::::::P  
F::::::::::::::::::::FT:::::::::::::::::::::TP::::::PPPPPP:::::P 
FF::::::FFFFFFFFF::::FT:::::TT:::::::TT:::::TPP:::::P     P:::::P
  F:::::F       FFFFFFTTTTTT  T:::::T  TTTTTT  P::::P     P:::::P
  F:::::F                     T:::::T          P::::P     P:::::P
  F::::::FFFFFFFFFF           T:::::T          P::::PPPPPP:::::P 
  F:::::::::::::::F           T:::::T          P:::::::::::::PP  
  F:::::::::::::::F           T:::::T          P::::PPPPPPPPP    
  F::::::FFFFFFFFFF           T:::::T          P::::P            
  F:::::F                     T:::::T          P::::P            
  F:::::F                     T:::::T          P::::P            
FF:::::::FF                 TT:::::::TT      PP::::::PP          
F::::::::FF                 T:::::::::T      P::::::::P          
F::::::::FF                 T:::::::::T      P::::::::P          
FFFFFFFFFFF                 TTTTTTTTTTT      PPPPPPPPPP
""" + "\033[0m")




init(autoreset=True)

SCAN_PROFILES = {
    "1": {"name": "Quick", "args": ["-T4", "--top-ports", "1000"]},
    "2": {"name": "Balanced", "args": ["-T4", "-sV"]},
    "3": {"name": "Aggressive", "args": ["-A", "-T4"]},
    "4": {"name": "Full", "args": ["-A", "-T4", "-p-"]},
}


def check_dependencies():
    if not shutil.which("nmap"):
        print(Fore.RED + "❌ Nmap is not installed.")
        exit(1)


def run_command(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def extract_open_ports(output):
    matches = re.findall(r"(\d+)/(tcp|udp)\s+open", output)
    return sorted(set(port for port, _ in matches))


def select_profile():
    print("\nSelect scan intensity:\n")
    for key, profile in SCAN_PROFILES.items():
        print(f"[{key}] {profile['name']}")

    choice = input("\nEnter choice: ").strip()
    if choice not in SCAN_PROFILES:
        print(Fore.RED + "Invalid selection.")
        exit(1)

    return SCAN_PROFILES[choice]


def main():
    print(BANNER)
    print(Fore.CYAN + "Automated Nmap Scanner")
    print(Fore.YELLOW + "⚠️ Scan only systems you own or have permission to test.\n")

    check_dependencies()

    target = input("Enter target IP or hostname: ").strip()
    profile = select_profile()

    use_proxy = input("\nUse proxychains? (y/N): ").lower() == "y"
    proxy_cmd = ["proxychains", "-q"] if use_proxy else []

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = f"scan_{timestamp}"

    print(
        Fore.GREEN
        + f"\n[+] Starting {profile['name'].upper()} scan on {target}...\n"
    )

    full_cmd = proxy_cmd + ["nmap"] + profile["args"] + [target]
    full_output = run_command(full_cmd)

    open_ports = extract_open_ports(full_output)

    with open(f"{base_name}_full.txt", "w") as f:
        f.write(full_output)

    results = {
        "target": target,
        "scan_type": profile["name"],
        "open_ports": open_ports,
        "timestamp": timestamp,
    }

    if open_ports:
        print(
            Fore.CYAN
            + f"[+] Open ports found: {', '.join(open_ports)}\n"
        )

        targeted_cmd = proxy_cmd + [
            "nmap",
            "-sC",
            "-sV",
            "-p",
            ",".join(open_ports),
            target,
        ]

        targeted_output = run_command(targeted_cmd)

        with open(f"{base_name}_targeted.txt", "w") as f:
            f.write(targeted_output)

        results["targeted_scan"] = targeted_output

    with open(f"{base_name}.json", "w") as f:
        json.dump(results, f, indent=4)

    print(Fore.GREEN + f"[✓] Scan completed. Files saved as {base_name}*")


if __name__ == "__main__":
    main()
