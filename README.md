# 📌 F7P-SHADOW Automated Nmap Scanner

[![Status](https://img.shields.io/badge/status-educational%20tool-yellow)](https://github.com/)
[![Language](https://img.shields.io/badge/language-Python-blue)](https://www.python.org/)
[![Nmap](https://img.shields.io/badge/tool-nmap-green)](https://nmap.org/)
[![License](https://img.shields.io/badge/license-UNLICENSE-lightgrey)](https://unlicense.org/)

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

- Performs a **full TCP port scan** on all ports (`-p-`)
- Automatically extracts **open ports**
- Runs a **targeted scan** on discovered open ports (`-sC`, `-sV`)
- Saves results to:
  - `full_scan.txt`
  - `targeted_scan.txt`

---

## ✅ Requirements

- Python 3.x  
- Nmap installed and available in PATH  

### Install Nmap (Linux)
```bash
sudo apt update
sudo apt install nmap
```

---

## 📥 Installation

```bash
git clone <your-repo-link>
cd <your-tool-folder>
```

---

## 🚀 Usage

```bash
python3 f7p_shadow_scanner.py
```

### Example
```
Enter the target IP: 192.168.1.1
```

Output files will be generated automatically:
- `full_scan.txt`
- `targeted_scan.txt`

---

## 🧠 How It Works

1. Runs a **full Nmap scan** (`-A`, `-T4`, `-p-`)
2. Extracts open TCP ports using regex
3. Runs a **targeted scan** on discovered ports (`-sC`, `-sV`)
4. Saves results to text files

---

## 🔧 Optional Improvements

If you want to make it more powerful:

- Add **error handling** for invalid IPs
- Support **IPv6**
- Add **custom scan options**
- Add **JSON/XML output**
- Add **argument parsing** with `argparse`
- Add **rate limiting / stealth options**

---

## 📝 License

This project is released under the **Unlicense** (public domain).

```
This is free and unlicensed software. See https://unlicense.org/
```
