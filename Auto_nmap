import subprocess
import re



print(r"""FFFFFFFFFFFFFFFFFFFFFFTTTTTTTTTTTTTTTTTTTTTTTPPPPPPPPPPPPPPPPP   
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
FFFFFFFFFFF                 TTTTTTTTTTT      PPPPPPPPPP""") 
print(r'automated nmap scan by F7P-SHADOW)
print()
print()







def run_nmap(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def save_output(filename, data):
    with open(filename, "w") as f:
        f.write(data)

def extract_open_ports(nmap_output):
    # Find lines like: "22/tcp   open  ssh"
    ports = re.findall(r"(\d+)/tcp\s+open", nmap_output)
    return ports

def main():
    target_ip = input("Enter the target IP: ")

    print("\nRunning FULL NMAP SCAN...\n")
    full_scan_cmd = ["nmap", "-A", "-T4", "-p-", "-oN", "full_scan.txt", target_ip]
    full_output = run_nmap(full_scan_cmd)

    save_output("full_scan.txt", full_output)

    print("Full scan completed. Results saved to full_scan.txt\n")

    open_ports = extract_open_ports(full_output)
    print("Open ports found:")
    print(open_ports)

    # If ports are found, run targeted scan
    if open_ports:
        port_list = ",".join(open_ports)
        print("\nRunning TARGETED scan on open ports...\n")

        targeted_scan_cmd = [
            "nmap",
            "-sC",
            "-sV",
            "-p",
            port_list,
            "-oN",
            "targeted_scan.txt",
            target_ip
        ]

        targeted_output = run_nmap(targeted_scan_cmd)
        save_output("targeted_scan.txt", targeted_output)

        print("Targeted scan completed. Results saved to targeted_scan.txt")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
