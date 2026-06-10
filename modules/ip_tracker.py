"""
IP Address Tracker Module
"""

import requests
from config import IP_API_PRIMARY, IP_API_SECONDARY, REQUEST_TIMEOUT
from colorama import Fore, Style
from tabulate import tabulate
import re

class IPTracker:
    def __init__(self):
        self.primary_api = IP_API_PRIMARY
        self.secondary_api = IP_API_SECONDARY
        self.timeout = REQUEST_TIMEOUT
    
    def get_ip_info(self, ip_address):
        try:
            response = requests.get(
                f"{self.primary_api}{ip_address}",
                timeout=self.timeout,
                params={'fields': 'status,country,countryCode,region,regionName,city,lat,lon,isp,org,as,asname,mobile,proxy,hosting,query'}
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return self.parse_ip_data(data)
            
            return self.get_ip_info_secondary(ip_address)
            
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[!] Error: {str(e)}{Style.RESET_ALL}")
            return None
    
    def get_ip_info_secondary(self, ip_address):
        try:
            response = requests.get(
                f"{self.secondary_api}{ip_address}/",
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json()
                return self.parse_secondary_data(data)
                
        except requests.exceptions.RequestException:
            print(f"{Fore.RED}[!] Secondary API failed{Style.RESET_ALL}")
            return None
    
    def parse_ip_data(self, data):
        parsed = {
            'ip': data.get('query'),
            'type': 'IPv4' if '.' in data.get('query', '') else 'IPv6',
            'country': data.get('country'),
            'country_code': data.get('countryCode'),
            'city': data.get('city'),
            'region': data.get('regionName'),
            'latitude': data.get('lat'),
            'longitude': data.get('lon'),
            'isp': data.get('isp'),
            'org': data.get('org'),
            'asn': data.get('as'),
            'asname': data.get('asname'),
            'mobile': data.get('mobile'),
            'proxy': data.get('proxy'),
            'hosting': data.get('hosting'),
            'maps_url': self.generate_maps_url(data.get('lat'), data.get('lon'))
        }
        return parsed
    
    def parse_secondary_data(self, data):
        parsed = {
            'ip': data.get('ip'),
            'type': 'IPv4' if '.' in data.get('ip', '') else 'IPv6',
            'country': data.get('country_name'),
            'country_code': data.get('country_code'),
            'city': data.get('city'),
            'region': data.get('region'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude'),
            'isp': data.get('isp'),
            'org': data.get('org'),
            'asn': data.get('asn'),
            'maps_url': self.generate_maps_url(data.get('latitude'), data.get('longitude'))
        }
        return parsed
    
    def generate_maps_url(self, lat, lon):
        if lat and lon:
            return f"https://www.google.com/maps/@{lat},{lon},10z"
        return "N/A"
    
    def display_results(self, data):
        if not data:
            print(f"{Fore.RED}[!] No data retrieved{Style.RESET_ALL}")
            return
        
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}IP INFORMATION{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")
        
        table_data = [
            ["IP Address", data.get('ip', 'N/A')],
            ["Type", data.get('type', 'N/A')],
            ["Country", data.get('country', 'N/A')],
            ["City", data.get('city', 'N/A')],
            ["Region", data.get('region', 'N/A')],
            ["Latitude", data.get('latitude', 'N/A')],
            ["Longitude", data.get('longitude', 'N/A')],
            ["ISP", data.get('isp', 'N/A')],
            ["Organization", data.get('org', 'N/A')],
            ["ASN", data.get('asn', 'N/A')],
            ["Maps", data.get('maps_url', 'N/A')]
        ]
        
        print(tabulate(table_data, headers=["Field", "Value"], tablefmt="grid"))
        print(f"\n{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")
    
    def validate_ip(self, ip):
        ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        return bool(re.match(ipv4_pattern, ip))