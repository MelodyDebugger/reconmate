# 🔍 ReconMate – Cybersecurity Recon Automation Tool

ReconMate is a Python-based tool that automates the reconnaissance phase of penetration testing. It integrates Nmap, Subfinder, and FFUF to collect information about a target and saves the results in structured reports.

---

## 🧠 Features

- Port scanning using **Nmap**
- Subdomain discovery using **Subfinder**
- Directory brute-forcing using **FFUF**
- Saves all results in a `/reports` folder

---

### 1. Clone the Repository
```bash
git clone https://github.com/MelodyDebugger/reconmate.git
cd reconmate
```

### 2. Run the Tool
```bash
python3 reconmate.py
```

### 3. Requirements
A. Check Python Version:
```bash
python3 --version
```
B. Install Nmap :
```bash
sudo apt install nmap
```
C. Install Subfinder :
```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```
D. Install FFUF :
```bash
sudo apt install ffuf
```
C. Wordlist :
```bash
/usr/share/wordlists/dirb/common.txt
```
### 4. Sample Output

- [Nmap Scan](hackerone_com_nmap.txt)
- [Subdomains](hackerone_com_subdomains.txt)
- [FFUF Results](hackerone_com_ffuf.txt)



