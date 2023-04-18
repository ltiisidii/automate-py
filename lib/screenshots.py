import subprocess
from pathlib import Path

class ScreenshotCapture:
    def __init__(self, hosts_file, results_dir, gowitness_threads):
        self.hosts_file = hosts_file
        self.results_dir = results_dir
        self.gowitness_threads = gowitness_threads
    
    def run(self):
        hosts = self.results_dir + "/hosts"
        screenshots = self.results_dir + "/screenshots"
        Path(screenshots).mkdir(parents=True, exist_ok=True)
        
        print('[+] Getting screenshots')
        try:
            subprocess.call(f'gowitness file -f {hosts}/{self.hosts_file} --output {screenshots} --disable-logging -t {self.gowitness_threads}', shell=True)
        except subprocess.CalledProcessError as e:
            print(f'Error running gowitness: {e}')
                   