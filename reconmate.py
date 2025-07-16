import subprocess
import os

# Create output folders if they don't exist
os.makedirs("reports", exist_ok=True)

# Ask user for target
target = input("Enter a domain or IP to scan: ").strip()

# Run Nmap scan
print(f"\n[+] Scanning {target} with Nmap...\n")
nmap_output_file = f"reports/{target.replace('.', '_')}_nmap.txt"

try:
    result = subprocess.run(
        ["nmap", "-sV", "-T4", "-oN", nmap_output_file, target],
        capture_output=True,
        text=True,
        check=True
    )
    print(f"[+] Nmap scan completed. Results saved to {nmap_output_file}")
except subprocess.CalledProcessError as e:
    print("[!] Nmap scan failed.")
    print(e.output)

# Function to check if input is a domain (not IP)
def is_domain(target):
    return any(c.isalpha() for c in target)

# Run Subfinder only if it's a domain
if is_domain(target):
    print(f"\n[+] Running subdomain enumeration on {target} using subfinder...\n")
    subdomain_output_file = f"reports/{target.replace('.', '_')}_subdomains.txt"
    
    try:
        result = subprocess.run(
            ["/home/kali/go/bin/subfinder", "-d", target, "-silent"],
            capture_output=True,
            text=True,
            check=True
        )
        subdomains = result.stdout.strip()
        
        if subdomains:
            with open(subdomain_output_file, "w") as f:
                f.write(subdomains)
            print(f"[+] Subdomains saved to {subdomain_output_file}")
        else:
            print("[!] No subdomains found.")
    
    except subprocess.CalledProcessError as e:
        print("[!] Subfinder failed.")
        print(e.output)

# Ask user if they want to perform directory brute-forcing
do_dirscan = input("\nDo you want to run directory brute-force on the target? (y/n): ").lower()

if do_dirscan == 'y':
    wordlist = "/usr/share/wordlists/dirb/common.txt"  # Default wordlist in Kali
    dir_output_file = f"reports/{target.replace('.', '_')}_ffuf.txt"
    
    print(f"\n[+] Running directory brute-force on {target} using ffuf...\n")

    try:
        result = subprocess.run(
            [
                "ffuf",
                "-u", f"http://{target}/FUZZ",
                "-w", wordlist,
                "-o", dir_output_file,
                "-of", "csv"
            ],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"[+] Directory scan completed. Results saved to {dir_output_file}")
    except subprocess.CalledProcessError as e:
        print("[!] ffuf failed.")
        print(e.output)
