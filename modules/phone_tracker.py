"""
Phone Number Tracker Module
"""

import phonenumbers
from phonenumbers import geocoder, carrier
from colorama import Fore, Style
from tabulate import tabulate

class PhoneTracker:
    def get_phone_info(self, phone_number, region=None):
        try:
            parsed = phonenumbers.parse(phone_number, region)
            
            if not phonenumbers.is_valid_number(parsed):
                print(f"{Fore.RED}[!] Invalid phone number format{Style.RESET_ALL}")
                return None
            
            country_code = parsed.country_code
            region_code = phonenumbers.region_code_for_number(parsed)
            carrier_name = carrier.name_for_number(parsed, 'en')
            location = geocoder.description_for_number(parsed, 'en')
            number_type = self.get_number_type(parsed)
            
            phone_info = {
                'original': phone_number,
                'country_code': f"+{country_code}",
                'region': region_code,
                'location': location,
                'carrier': carrier_name if carrier_name else 'Unknown',
                'type': number_type,
                'is_valid': phonenumbers.is_valid_number(parsed),
                'formatted_e164': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164),
                'formatted_international': phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            }
            
            return phone_info
            
        except phonenumbers.NumberParseException as e:
            print(f"{Fore.RED}[!] Error parsing: {str(e)}{Style.RESET_ALL}")
            return None
    
    def get_number_type(self, parsed_number):
        number_type = phonenumbers.number_type(parsed_number)
        type_map = {0: 'Fixed Line', 1: 'Mobile', 2: 'Fixed/Mobile', 3: 'Toll Free', 4: 'Premium', 6: 'VOIP'}
        return type_map.get(number_type, 'Unknown')
    
    def display_results(self, data):
        if not data:
            print(f"{Fore.RED}[!] No data retrieved{Style.RESET_ALL}")
            return
        
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}PHONE INFORMATION{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")
        
        table_data = [
            ["Phone", data.get('original', 'N/A')],
            ["Country Code", data.get('country_code', 'N/A')],
            ["Region", data.get('region', 'N/A')],
            ["Location", data.get('location', 'N/A')],
            ["Carrier", data.get('carrier', 'N/A')],
            ["Type", data.get('type', 'N/A')],
            ["Valid", "✓ Yes" if data.get('is_valid') else "✗ No"],
            ["E.164", data.get('formatted_e164', 'N/A')],
        ]
        
        print(tabulate(table_data, headers=["Field", "Value"], tablefmt="grid"))
        print(f"\n{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")