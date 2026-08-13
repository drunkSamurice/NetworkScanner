#!/usr/bin/env python3
import socket
import subprocess
import platform
from datetime import datetime

def get_host_info():
    current_date_time = datetime.now()
    return current_date_time

def print_host_info():
    current_date_time = get_host_info()
    print("\n" + "-"*60)
    print(f"Date and Time: {current_date_time}")
    print("-"*60 + "\n")

def vanilla_scan(base_ip, start, end):
    print("\n" + "-"*60)
    print("VANILLA SCAN - HOST DISCOVERY")
    print("-"*60)
    print(f"\nIP Address: {base_ip}.0")
    print(f"Starting IP Number: {start}")
    print(f"Ending IP Number: {end}")
    print(f"Total IPs to scan: {end - start + 1}")
    print("\nScanning in progress...\n")
    
    live_hosts = []
    scanned_count = 0
    
    for i in range(start, end + 1):
        ip = f"{base_ip}.{i}"
        scanned_count += 1
        
        # Show progress every 10 IPs
        if scanned_count % 10 == 0:
            print(f"[Progress] Scanned {scanned_count}/{end - start + 1} IPs...", end='\r')
        
        # Try TCP 
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            result = sock.connect_ex((ip, 22))
            sock.close()
            
            if result == 0:
                print(f"{ip} is live                                    ")
                live_hosts.append(ip)
                continue
        except:
            pass
        
        # Try ping
        try:
            if platform.system().lower() == "windows":
                output = subprocess.run(
                    ["ping", "-n", "1", "-w", "500", ip],
                    capture_output=True,
                    timeout=1
                )
            else:
                output = subprocess.run(
                    ["ping", "-c", "1", "-W", "500", ip],
                    capture_output=True,
                    timeout=1
                )
            
            if output.returncode == 0:
                print(f"{ip} is live                                    ")
                live_hosts.append(ip)
        except:
            pass
    
    print(f"\n{'-'*60}")
    print(f"VANILLA SCAN COMPLETE")
    print(f"Scanned: {scanned_count} IPs")
    print(f"Live hosts found: {len(live_hosts)}")
    if live_hosts:
        print(f"Hosts: {', '.join(live_hosts)}")
    print(f"{'-'*60}")
    
    print_host_info()
    return live_hosts
