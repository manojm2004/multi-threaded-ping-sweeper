"""
CEH Network Reconnaissance & Service Banner Scanner
Author: Manoj M | Network & Cyber Security Engineer
Alignment: EC-Council CEH Module 3 (Scanning Networks)
"""

import socket
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet (Insecure)",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

def scan_port(host, port, service):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        result = sock.connect_ex((host, port))
        if result == 0:
            banner = ""
            try:
                sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = sock.recv(100).decode("utf-8", errors="ignore").strip().split("\n")[0]
            except Exception:
                pass
            print(f"[+] OPEN: Port {port:5d} ({service:20s}) | Banner: {banner}")
        sock.close()
    except Exception:
        pass

def run_recon(target):
    print("="*65)
    print(f"🎯 CEH RECONNAISSANCE SCANNER FOR: {target}")
    print("="*65)
    with ThreadPoolExecutor(max_workers=20) as executor:
        for p, s in COMMON_PORTS.items():
            executor.submit(scan_port, target, p, s)

if __name__ == "__main__":
    run_recon("127.0.0.1")
