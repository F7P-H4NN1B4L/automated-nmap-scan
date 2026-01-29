# 📌 F7P-H4NN1B4L Automated Nmap Scanner


[![Status](https://img.shields.io/badge/status-educational%20tool-yellow)](https://github.com/)
[![Language](https://img.shields.io/badge/language-Python-blue)](https://www.python.org/)
[![Nmap](https://img.shields.io/badge/tool-nmap-green)](https://nmap.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)


---


## ⚠️ Disclaimer (Read Before Use)


This tool is **for educational purposes only** and should only be used in **authorized environments** such as:


- Your own lab environment  
- A CTF challenge  
- A written penetration test engagement with explicit permission  


**Do NOT scan targets you do not own or have permission to test.**  
Unauthorized scanning is illegal and unethical. The author is not responsible for misuse.


---


## 🧰 Features


- Interactive **menu-based interface**
- Multiple **scan intensity profiles**
  - Quick
  - Balanced
  - Aggressive
  - Full
- Full TCP port scanning and targeted service detection
- Automatic extraction of open ports
- Colored terminal output
- Optional JSON export
- Timestamped output files
- Installable as a system-wide CLI tool


---


## ✅ Requirements


- Python 3.9+  
- Nmap installed and available in PATH  


### Install Nmap (Linux)
  bash
  sudo apt update
  sudo apt install nmap
  📦 Installation (Recommended)
  git clone <your-repo-link>
  cd <your-tool-folder>
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  pip install -e .

After installation, the tool can be run globally:

f7pscanner
## 🚀 Usage

Run the tool and follow the interactive menu:

f7pscanner

Example:

Enter target IP or hostname: 192.168.1.1


Select scan intensity:
[1] Quick
[2] Balanced
[3] Aggressive
[4] Full


Enter choice: 4
## 📁 Output

The tool automatically saves results:

scan_<timestamp>_full.txt

scan_<timestamp>_targeted.txt

scan_<timestamp>.json (optional)

## 🧠 How It Works

User selects target and scan intensity

A full scan is executed based on the selected profile

Open ports are extracted automatically

A targeted scan runs on discovered ports

Results are saved to disk for later analysis

## 📝 License

This project is licensed under the MIT License.

## Have any problem contact me: Z3R0D4Y@tutamail.com
      Z3R0D4Y@tutamail.com

<p> <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=40&duration=2500&pause=800&color=FF0000&center=true&vCenter=true&width=650&lines=%E2%98%A0%EF%B8%8F+Z3R0D4Y+TEAM" /> <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=40&duration=2500&pause=800&color=FFFFFF&center=true&vCenter=true&width=650&lines=Learn.+Break.+Defend." /> </p>
