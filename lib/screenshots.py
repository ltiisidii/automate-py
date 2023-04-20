import subprocess
from pathlib import Path

class ScreenshotCapture:
    def __init__(self, domain, hosts_file="public_hosts.txt", results_dir="results/", gowitness_threads=50):
        self.domain = domain
        self.hosts_file = hosts_file
        self.results_dir = results_dir
        self.gowitness_threads = gowitness_threads
    
    def run(self):
        hosts = f"{self.results_dir}{self.domain}/subdomains"
        screenshots = f"{self.results_dir}{self.domain}/screenshots/"
        Path(screenshots).mkdir(parents=True, exist_ok=True)
        
        print('[+] Getting screenshots')
        try:
            # sudo apt install chromium-browser
            subprocess.call(f'gowitness file -f {hosts}/{self.hosts_file} -t {self.gowitness_threads} --user-agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36" -P {screenshots} --chrome-path "/usr/bin/google-chrome-stable"', shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error running gowitness: {e}')