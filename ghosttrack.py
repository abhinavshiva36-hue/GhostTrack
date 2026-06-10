#!/usr/bin/env python3
"""
ABHINAV TRACKER - OSINT Intelligence Tool
IP, Phone & Username Tracker
"""

import os
import sys
from colorama import Fore, Style, init

init(autoreset=False)

from modules.ip_tracker import IPTracker
from modules.phone_tracker import PhoneTracker
from modules.username_tracker import UsernameTracker
from modules.reverse_lookup import ReverseIPLookup

VERSION = "1.0.0"
AUTHOR = "abhinavshiva36-hue"

class ABHINAVTracker:
    def __init__(self):
        self.ip_tracker = IPTracker()
        self.phone_tracker = PhoneTracker()
        self.username_tracker = UsernameTracker()
        self.reverse_lookup = ReverseIPLookup()
    
    def display_banner(self):
        banner = f"""
{Fore.RED}
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║{Fore.YELLOW}  █████╗ ██████╗ ██╗  ██╗██╗███╗   ██╗ █████╗ ██╗   ██╗{Style.RESET_ALL}{Fore.RED}  ║
║{Fore.YELLOW} ██╔══██╗██╔══██╗██║  ██║██║████╗  ██║██╔══██╗██║   ██║{Style.RESET_ALL}{Fore.RED}  ║
║{Fore.YELLOW} ███████║██████╔╝███████║██║██╔██╗ ██║███████║██║   ██║{Style.RESET_ALL}{Fore.RED}  ║
║{Fore.YELLOW} ██╔══██║██╔══██╗██╔══██║██║██║╚██╗██║██╔══██║╚██╗ ██╔╝{Style.RESET_ALL}{Fore.RED}  ║
║{Fore.YELLOW} ██║  ██║██████╔╝██║  ██║██║██║ ╚████║██║  ██║ ╚████╔╝{Style.RESET_ALL}{Fore.RED}   ║
║{Fore.YELLOW} ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝{Style.RESET_ALL}{Fore.RED}    ║
║                                                                ║
║{Fore.CYAN}              ████████╗██████╗  █████╗  ██████╗███████╗{Style.RESET_ALL}{Fore.RED}      ║
║{Fore.CYAN}              ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝{Style.RESET_ALL}{Fore.RED}      ║
║{Fore.CYAN}                 ██║   ██████╔╝███████║██║     █████╗{Style.RESET_ALL}{Fore.RED}        ║
║{Fore.CYAN}                 ██║   ██╔══██╗██╔══██║██║     ██╔══╝{Style.RESET_ALL}{Fore.RED}        ║
║{Fore.CYAN}                 ██║   ██║  ██║██║  ██║╚██████╗███████╗{Style.RESET_ALL}{Fore.RED}      ║
║{Fore.CYAN}                 ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝{Style.RESET_ALL}{Fore.RED}      ║
║                                                                ║
║{Fore.GREEN}           POWERFUL OSINT INTELLIGENCE TOOL v{VERSION}{Style.RESET_ALL}{Fore.RED}             ║
║{Fore.GREEN}              IP • Phone • Username Tracker{Style.RESET_ALL}{Fore.RED}                  ║
║{Fore.YELLOW}                   by {AUTHOR}{Style.RESET_ALL}{Fore.RED}                   ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
"""
        print(banner)
    
    def display_menu(self):
        menu = f"""
{Fore.CYAN}┌─────────────────────────────────────────┐{Style.RESET_ALL}
{Fore.CYAN}│{Style.RESET_ALL}{Fore.YELLOW}      SELECT TRACKING OPTION{Style.RESET_ALL}{Fore.CYAN}        │{Style.RESET_ALL}
{Fore.CYAN}├─────────────────────────────────────────┤{Style.RESET_ALL}
{Fore.CYAN}│{Style.RESET_ALL}
{Fore.CYAN}│{Style.RESET_ALL}  {Fore.GREEN}[1]{Style.RESET_ALL} 🌍 IP Address Tracker
{Fore.CYAN}│{Style.RESET_ALL}  {Fore.GREEN}[2]{Style.RESET_ALL} 📱 Phone Number Tracker
{Fore.CYAN}│{Style.RESET_ALL}  {Fore.GREEN}[3]{Style.RESET_ALL} 👤 Username Tracker
{Fore.CYAN}│{Style.RESET_ALL}  {Fore.GREEN}[4]{Style.RESET_ALL} 🔍 Reverse IP Lookup
{Fore.CYAN}│{Style.RESET_ALL}  {Fore.RED}[0]{Style.RESET_ALL} ❌ Exit
{Fore.CYAN}│{Style.RESET_ALL}
{Fore.CYAN}└─────────────────────────────────────────┘{Style.RESET_ALL}
"""
        print(menu)
    
    def ip_tracker_menu(self):
        print(f"\n{Fore.GREEN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🌍 IP ADDRESS TRACKER{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}[*] Enter IP address (e.g., 8.8.8.8){Style.RESET_ALL}")
        ip = input(f"{Fore.YELLOW}→ {Style.RESET_ALL}").strip()
        
        if not ip:
            print(f"{Fore.RED}[!] Invalid input{Style.RESET_ALL}")
            return
        
        print(f"{Fore.CYAN}[*] Fetching information...{Style.RESET_ALL}\n")
        data = self.ip_tracker.get_ip_info(ip)
        if data:
            self.ip_tracker.display_results(data)
        else:
            print(f"{Fore.RED}[!] Failed to retrieve information{Style.RESET_ALL}\n")
    
    def phone_tracker_menu(self):
        print(f"\n{Fore.GREEN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}📱 PHONE NUMBER TRACKER{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}[*] Enter phone number (e.g., +919876543210){Style.RESET_ALL}")
        phone = input(f"{Fore.YELLOW}→ {Style.RESET_ALL}").strip()
        
        if not phone:
            print(f"{Fore.RED}[!] Invalid input{Style.RESET_ALL}")
            return
        
        print(f"{Fore.CYAN}[*] Analyzing phone number...{Style.RESET_ALL}\n")
        data = self.phone_tracker.get_phone_info(phone)
        if data:
            self.phone_tracker.display_results(data)
        else:
            print(f"{Fore.RED}[!] Failed to retrieve information{Style.RESET_ALL}\n")
    
    def username_tracker_menu(self):
        print(f"\n{Fore.GREEN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}👤 USERNAME TRACKER{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}[*] Enter username to search (min 2 chars){Style.RESET_ALL}")
        username = input(f"{Fore.YELLOW}→ {Style.RESET_ALL}").strip()
        
        if not username or len(username) < 2:
            print(f"{Fore.RED}[!] Invalid input{Style.RESET_ALL}")
            return
        
        print(f"{Fore.CYAN}[*] Searching across 15+ platforms...{Style.RESET_ALL}")
        results = self.username_tracker.search_username(username, max_workers=8)
        self.username_tracker.display_results(results)
    
    def reverse_lookup_menu(self):
        print(f"\n{Fore.GREEN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🔍 REVERSE IP/DNS LOOKUP{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}[1] Reverse DNS (IP → Hostname)")
        print(f"{Fore.CYAN}[2] Forward DNS (Hostname → IP)")
        print(f"{Fore.CYAN}[3] DNS Records Lookup\n{Style.RESET_ALL}")
        
        choice = input(f"{Fore.YELLOW}→ {Style.RESET_ALL}").strip()
        
        if choice == '1':
            ip = input(f"{Fore.CYAN}Enter IP: {Style.RESET_ALL}").strip()
            if ip:
                print(f"{Fore.CYAN}[*] Performing reverse DNS lookup...{Style.RESET_ALL}\n")
                hostnames = self.reverse_lookup.get_reverse_dns(ip)
                self.reverse_lookup.display_reverse_dns_results(ip, hostnames)
        
        elif choice == '2':
            hostname = input(f"{Fore.CYAN}Enter hostname: {Style.RESET_ALL}").strip()
            if hostname:
                print(f"{Fore.CYAN}[*] Resolving hostname...{Style.RESET_ALL}\n")
                result = self.reverse_lookup.get_forward_dns(hostname)
                if result:
                    print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}FORWARD DNS RESULT{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")
                    print(f"{Fore.GREEN}IP Addresses: {Fore.YELLOW}{', '.join(result['ip_addresses'])}{Style.RESET_ALL}\n")
                else:
                    print(f"{Fore.RED}[!] Could not resolve hostname{Style.RESET_ALL}\n")
        
        elif choice == '3':
            domain = input(f"{Fore.CYAN}Enter domain: {Style.RESET_ALL}").strip()
            if domain:
                print(f"{Fore.CYAN}[*] Fetching DNS records...{Style.RESET_ALL}\n")
                records = self.reverse_lookup.get_dns_records(domain)
                self.reverse_lookup.display_dns_records(domain, records)
        else:
            print(f"{Fore.RED}[!] Invalid option{Style.RESET_ALL}\n")
    
    def run(self):
        while True:
            os.system('clear') if os.name == 'posix' else os.system('cls')
            
            self.display_banner()
            self.display_menu()
            
            choice = input(f"{Fore.YELLOW}Select option: {Style.RESET_ALL}").strip()
            
            if choice == '1':
                self.ip_tracker_menu()
            elif choice == '2':
                self.phone_tracker_menu()
            elif choice == '3':
                self.username_tracker_menu()
            elif choice == '4':
                self.reverse_lookup_menu()
            elif choice == '0':
                print(f"\n{Fore.RED}{'='*50}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}[*] Thank you for using ABHINAV TRACKER!{Style.RESET_ALL}")
                print(f"{Fore.RED}{'='*50}{Style.RESET_ALL}\n")
                sys.exit(0)
            else:
                print(f"{Fore.RED}[!] Invalid option. Please try again.{Style.RESET_ALL}")
            
            input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")

def main():
    try:
        app = ABHINAVTracker()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[*] Interrupted by user{Style.RESET_ALL}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()