# 🎯 CEH Network Scanning & Reconnaissance Methodology
**Author:** Manoj M | Network & Cyber Security Engineer  
**Alignment:** EC-Council CEH Module 3 (Scanning Networks)

---

## 📌 1. Nmap Scanning Commands & Techniques

| Scanning Technique | Nmap Command | Explanation |
| :--- | :--- | :--- |
| **TCP SYN Stealth Scan** | `nmap -sS -T4 <target>` | Default CEH scan. Sends SYN, receives SYN-ACK, immediately sends RST. Does not complete 3-way handshake; evasive to legacy logs. |
| **TCP Connect Scan** | `nmap -sT <target>` | Completes full 3-way handshake (SYN, SYN-ACK, ACK). Used when raw socket privileges are unavailable. |
| **Service & Version Scan** | `nmap -sV --version-intensity 5 <target>` | Probes open ports with payloads to fingerprint exact daemon software and version (e.g., Apache 2.4.41). |
| **OS Fingerprinting** | `nmap -O <target>` | Analyzes TCP/IP stack implementation nuances (window size, TTL, TCP options) to determine underlying OS. |
| **Vulnerability Script Scan** | `nmap -sC --script=vuln <target>` | Leverages Nmap Scripting Engine (NSE) to automatically test for known CVE vulnerabilities. |
| **UDP Port Scan** | `nmap -sU -p 53,67,69,123,161 <target>` | Identifies open UDP services like DNS, DHCP, TFTP, NTP, and SNMP. |

---

## 📌 2. Evading Firewalls & IDS (CEH Module 12)
```bash
# Fragment packets to bypass stateful packet inspection
nmap -f <target>

# Spoof Source IP Address
nmap -S <spoofed_ip> -e eth0 <target>

# Decoy Scanning (Mask real scanning IP among multiple legitimate IPs)
nmap -D 192.168.1.5,192.168.1.7,ME <target>

# Scan with custom Source Port (e.g. DNS port 53 to bypass inbound rules)
nmap --source-port 53 <target>
```
