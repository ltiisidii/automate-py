import subprocess
from pathlib import Path

class Nuclei:
    def __init__(self, hosts_file, results_dir, threads=50, rate_limit=150):
        self.hosts_file = hosts_file
        self.results_dir = results_dir
        self.threads = threads
        self.rate_limit = rate_limit

    def run_template(self, template_name, output_file):
        print(f"[+] Running Nuclei Template {template_name}")
        try:
            subprocess.call(f"nuclei -l {self.hosts_file} -t {template_name} -o {self.results_dir}/{output_file} -c {self.threads} -rate-limit {self.rate_limit}", shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running nuclei: {e}")
            
    def run_all_templates(self):
        templates = [
            "cves",
            "default-credentials",
            "dns",
            "files",
            "panels",
            "security-misconfiguration",
            "subdomain-takeover",
            "technologies",
            "tokens",
            "vulnerabilities",
        ]
        for template in templates:
            self.run_template(template, f"{template}.txt")