import sys
import subprocess
import ipaddress
import platform
from concurrent.futures import ThreadPoolExecutor

def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    timeout_param = "-w" if platform.system().lower() == "windows" else "-W"
    cmd = ["ping", param, "1", timeout_param, "1000", str(ip)]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if res.returncode == 0:
        print(f" [ONLINE] Host: {ip}")
        return str(ip)
    return None

def sweep(subnet_str, max_workers=30):
    net = ipaddress.ip_network(subnet_str, strict=False)
    print(f"Starting sweep across {net} with {max_workers} threads...")
    live_hosts = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(ping_host, net.hosts())
        live_hosts = [h for h in results if h]
    print(f"\nSweep Complete: {len(live_hosts)} hosts online.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1/32"
    sweep(target)
