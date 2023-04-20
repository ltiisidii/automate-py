import subprocess
from pathlib import Path

class IPDiscovery:
    def __init__(self, hosts_file, results_dir):
        self.hosts_file = hosts_file
        self.results_dir = results_dir
    
    def run(self):
        hosts = self.results_dir + "/hosts"
        ips = self.results_dir + "/ips"
        Path(ips).mkdir(parents=True, exist_ok=True)
        
        print('[+] Getting IPs')
        try:
            #subprocess.check_call(f'dnsprobe -l {hosts}/{self.hosts_file} | sed \'s/^[^[:space:]]*[[:space:]]*//\' | sed \'/^$/d\' | sort -u > {ips}/dnsprobe.txt', shell=True)
            subprocess.check_call(f"dnsx -l {hosts}/{self.hosts_file} -silent -resp-only | awk '{{print $$NF}}' | sort -u > {ips}/dnsx-ips.txt", shell=True)

        except subprocess.CalledProcessError as e:
            print(f'Error running dnsprobe: {e}')