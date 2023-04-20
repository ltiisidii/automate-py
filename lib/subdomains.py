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
            subprocess.call(f'amass enum -passive -d' + ' ' + self.domain + ' ' + '-timeout ' + str(self.amass_enum_timeout) + ' ' + '-o ' + ' ' + self.subs + '/amass-passive.txt'
                        , shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error running amass: {e}')
        
        print('[+] Combining and sorting subdomains')
        try:
            subprocess.call(f'cat' + ' ' + self.subs + '/*.txt | sort -u >' + ' ' + self.subs + '/subdomains.txt'
                        , shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error combining and sorting subdomains: {e}')


        # Check for publicly accessible hosts using httpx
        print('[+] Checking for publicly accessible hosts')
        try:
            subprocess.call(f'httpx -l {self.subs}/subdomains.txt -silent -threads 9000 -timeout 30 -status-code 200 | cut -d " " -f 1 | sort -u > {self.subs}/public_hosts.txt', shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error checking for publicly accessible hosts: {e}')

        # Get IPs with dnsprobe
        print('[+] Getting IPs')
        try:
            subprocess.call(f'dnsx -resp-only -l {self.subs}/subdomains.txt > {self.subs}/ips-from-dns.txt', shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error getting IPs: {e}')