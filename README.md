# ⚡ High-Speed Multi-Threaded Ping Sweeper

A Python utility built with `concurrent.futures` to rapidly discover active hosts across an entire subnet (e.g., `/24`) in seconds.

## 🚀 Key Capabilities
- Multi-threaded ICMP ping execution.
- Cross-platform support (Windows & Linux ping flags).
- Exports live host report with response latency into CSV.

## 💻 Usage
```bash
python ping_sweeper.py 192.168.1.0/24 --workers 50
```
