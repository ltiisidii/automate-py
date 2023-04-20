import subprocess
from pathlib import Path

class HostDetection:    
    def __init__(self, subs_file, results_dir, httpx_threads=100, httpx_ratelimit=50, httpx_timeout=10):
        self.subs_file = subs_file
        self.results_dir = results_dir
        self.httpx_threads = httpx_threads
        self.httpx_ratelimit = httpx_ratelimit
        self.httpx_timeout = httpx_timeout
    
    def run(self):
        subs = self.results_dir + "results"
        hosts = self.results_dir + "/hosts"
        Path(hosts).mkdir(parents=True, exist_ok=True)
        
        print('[+] Getting alive hosts')
        try:
            subprocess.call(f'httpx -l {subs}/{self.subs_file} -silent -threads {self.httpx_threads} -rate-limit {self.httpx_ratelimit} -timeout {self.httpx_timeout} -o {hosts}/httpx.txt', shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error running httpx: {e}')