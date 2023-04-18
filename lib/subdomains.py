import subprocess
from pathlib import Path

class Subdomains:
    def __init__(self, domain):
        self.domain = domain
        self.create_assets = "results"
        self.resultdir = self.create_assets + "/" + domain
        self.subs = self.resultdir + "/subdomains"
        self.screenshots = self.resultdir + "/screenshots"
        self.nuclei = self.resultdir + "/nuclei"

        self.amass_config = "~/.config/amass/config.ini"
        self.amass_enum_timeout = 180

        # Create directories
        Path(self.create_assets).mkdir(parents=True, exist_ok=True)
        Path(self.resultdir).mkdir(parents=True, exist_ok=True)
        Path(self.subs).mkdir(parents=True, exist_ok=True)
        Path(self.screenshots).mkdir(parents=True, exist_ok=True)
        Path(self.nuclei).mkdir(parents=True, exist_ok=True)

    def run(self):
        # Subdomains
        print('[+] Execting subdomains')

        print('[+] 1- Running subfinder')
        try:
            subprocess.call(f'subfinder -d' + ' ' + self.domain + ' ' + '-all -o ' + self.subs + '/subfinder.txt'
                        , shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error running subfinder: {e}')

        print('[+] 2- Running amass')
        try:
            subprocess.call(f'amass enum -passive -d' + ' ' + self.domain + ' ' + self.amass_config + ' ' + '-timeout' + self.amass_enum_timeout + ' ' + '-o' + ' ' + self.subs + '/amassp.txt'
                        , shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error running amass: {e}')
        
        print('[+] Combining and sorting subdomains')
        try:
            subprocess.call(f'cat' + ' ' + self.subs + '/*.txt | sort -u >' + ' ' + self.subs + '/subdomains.txt'
                        , shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error combining and sorting subdomains: {e}')


        # Alive hosts
        print('[+] Getting alive hosts')
        try:
            subprocess.call(f'httpx -l' + ' ' + self.subs + '/subdomains.txt' + ' ' + '-silent -threads 9000 -timeout 30 | anew' + ' ' + self.subs + '/hosts.txt'
                        , shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error getting alive hosts: {e}')

        # Get IPs with dnsprobe
        print('[+] Getting IPs')
        try:
            subprocess.call(f'dnsx -l' + ' ' + self.subs + '/hosts.txt' + ' ' + '-o' + ' ' + self.subs + '/ips.txt'
                        , shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error getting IPs: {e}')
            