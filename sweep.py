#!/usr/bin/env python3
import socket
from vanilla import print_host_info

def sweep_scan(target_host, start_port, end_port):
    print("\n" + "-"*60)
    print("SWEEP SCAN - PORT SCANNING")
    print("-"*60)
    print(f"\nEnter the host to be scanned: {target_host}")
    print(f"Starting scan on host: {target_host}")
    print(f"Port range: {start_port}-{end_port}")
    print(f"Total ports to scan: {end_port - start_port + 1}")
    print("\nScanning in progress...\n")
    
    open_ports = []
    scanned_count = 0
    
    for port in range(start_port, end_port + 1):
        scanned_count += 1
        
        # Show progress
        if scanned_count % 10 == 0:
            print(f"[Progress] Scanned {scanned_count}/{end_port - start_port + 1} ports...", end='\r')
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.2)
            result = sock.connect_ex((target_host, port))
            sock.close()
            
            if result == 0:
                print(f"{port} is open                                    ")
                open_ports.append(port)
        except Exception as e:
            pass
    
    print(f"\n{'-'*60}")
    print(f"SWEEP SCAN COMPLETE")
    print(f"Scanned: {scanned_count} ports")
    print(f"Open ports found: {len(open_ports)}")
    if open_ports:
        print(f"Ports: {', '.join(map(str, open_ports))}")
    print(f"{'-'*60}")
    
    print_host_info()
    return open_ports
