"""
Reverse IP Lookup Module
"""

import socket
import dns.resolver
import dns.reversename
from colorama import Fore, Style
from tabulate import tabulate

class ReverseIPLookup:
    def get_reverse_dns(self, ip_address):
        try:
            reverse_ip = dns.reversename.from_address(ip_address)
            answers = dns.resolver.resolve(reverse_ip, "PTR")
            return [str(rdata).rstrip('.') for rdata in answers]
        except:
            return None
    
    def get_forward_dns(self, hostname):
        try:
            ips = socket.gethostbyname_ex(hostname)
            return {'hostname': ips[0], 'ip_addresses': ips[2]}
        except:
            return None
    
    def get_dns_records(self, domain):
        dns_records = {}
        for record_type in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                dns_records[record_type] = [str(rdata) for rdata in answers]
            except:
                dns_records[record_type] = None
        return dns_records
    
    def display_reverse_dns_results(self, ip_address, hostnames):
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}REVERSE DNS: {ip_address}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")
        
        if hostnames:
            for idx, hostname in enumerate(hostnames, 1):
                print(f"{Fore.GREEN}[{idx}]{Style.RESET_ALL} {Fore.YELLOW}{hostname}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[*] No records found{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")
    
    def display_dns_records(self, domain, records):
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}DNS RECORDS: {domain}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")
        
        table_data = []
        for record_type, values in records.items():
            if values:
                value_str = ', '.join(values[:2])
                if len(values) > 2:
                    value_str += f" (+{len(values)-2})"
                table_data.append([record_type, "Found", value_str])
            else:
                table_data.append([record_type, "None", "N/A"])
        
        print(tabulate(table_data, headers=["Type", "Status", "Values"], tablefmt="grid"))
        print(f"\n{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")