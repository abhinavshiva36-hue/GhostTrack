"""
Username Tracker Module
"""

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style

class UsernameTracker:
    def __init__(self):
        self.platforms = {
            'Instagram': 'https://www.instagram.com/{}/',
            'Twitter': 'https://www.twitter.com/{}/',
            'TikTok': 'https://www.tiktok.com/@{}',
            'GitHub': 'https://www.github.com/{}/',
            'Facebook': 'https://www.facebook.com/{}/',
            'YouTube': 'https://www.youtube.com/@{}',
            'LinkedIn': 'https://www.linkedin.com/in/{}/',
            'Reddit': 'https://www.reddit.com/user/{}/',
            'Twitch': 'https://www.twitch.tv/{}',
            'Pinterest': 'https://www.pinterest.com/{}/',
            'Telegram': 'https://t.me/{}',
            'Medium': 'https://medium.com/@{}',
            'Tumblr': 'https://{}.tumblr.com',
            'Snapchat': 'https://www.snapchat.com/add/{}',
            'Discord': 'https://discordapp.com/users/search?username={}',
        }
        self.timeout = 8
    
    def check_username(self, platform, username):
        try:
            url = self.platforms[platform].format(username)
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=self.timeout)
            return response.status_code == 200
        except:
            return False
    
    def search_username(self, username, max_workers=5):
        print(f"\n{Fore.CYAN}Searching: {Fore.YELLOW}{username}{Style.RESET_ALL}\n")
        
        found_accounts = {}
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(self.check_username, platform, username): platform
                for platform in self.platforms.keys()
            }
            
            for future in as_completed(futures):
                platform = futures[future]
                try:
                    if future.result():
                        found_accounts[platform] = self.platforms[platform].format(username)
                        print(f"{Fore.GREEN}✓{Style.RESET_ALL} {platform}")
                    else:
                        print(f"{Fore.RED}✗{Style.RESET_ALL} {platform}")
                except:
                    print(f"{Fore.RED}✗{Style.RESET_ALL} {platform}")
        
        return found_accounts
    
    def display_results(self, accounts):
        if not accounts:
            print(f"\n{Fore.YELLOW}[*] No accounts found{Style.RESET_ALL}\n")
            return
        
        print(f"\n{Fore.GREEN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}FOUND ON {len(accounts)} PLATFORM(S){Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")
        
        for idx, (platform, url) in enumerate(sorted(accounts.items()), 1):
            print(f"{Fore.GREEN}[{idx}]{Style.RESET_ALL} {Fore.CYAN}{platform}{Style.RESET_ALL}")
            print(f"    {Fore.YELLOW}→ {url}{Style.RESET_ALL}\n")
        
        print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}\n")