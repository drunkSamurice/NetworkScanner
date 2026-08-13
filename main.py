#!/usr/bin/env python3
from vanilla import vanilla_scan
from sweep import sweep_scan

if __name__ == "__main__":
    print("\n" + "-"*60)
    print("NETWORK SCANNING TOOL - Lab 4 [VERBOSE]")
    print("-"*60)
    
    while True:
        print("\nSelect scanning mode:")
        print("1. Vanilla Scan (Host Discovery)")
        print("2. Sweep Scan (Port Scanning)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            try:
                base_ip = input("\nEnter base IP (e.g., 192.168.16): ").strip()
                start = int(input("Enter starting number (e.g., 1): ").strip())
                end = int(input("Enter ending number (e.g., 100): ").strip())
                
                if start < 1 or end > 255 or start > end:
                    print("Invalid range! Use 1-255")
                else:
                    vanilla_scan(base_ip, start, end)
                    input("\nPress Enter to continue...")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            try:
                host = input("\nEnter target host IP (e.g., 192.168.16.254): ").strip()
                start_port = int(input("Enter starting port (e.g., 80): ").strip())
                end_port = int(input("Enter ending port (e.g., 464): ").strip())
                
                if start_port < 1 or end_port > 65535 or start_port > end_port:
                    print("Invalid port range! Use 1-65535")
                else:
                    sweep_scan(host, start_port, end_port)
                    input("\nPress Enter to continue...")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")
