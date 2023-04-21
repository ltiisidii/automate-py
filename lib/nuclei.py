import subprocess
import configparser
from pathlib import Path

class Nuclei:
    def __init__(self, domain, config_file="config/automate-py.ini"):
        config = configparser.ConfigParser()
        config.read(config_file)
        
        self.domain = domain
        self.hosts_file = config.get("nuclei", "hosts_file").replace("{domain}", self.domain)
        self.results_dir = config.get("nuclei", "results_dir").replace("{domain}", self.domain)
        self.threads = config.getint("nuclei", "threads")
        self.rate_limit = config.getint("nuclei", "rate_limit")

        # Create directories
        Path(self.results_dir).mkdir(parents=True, exist_ok=True)

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
        severity_map = {
            "informational": "informative.txt",
            "low": "low.txt",
            "medium": "medium.txt",
            "high": "high.txt",
            "critical": "critical.txt"
        }
        for template in templates:
            for severity, file_name in severity_map.items():
                output_file = f"{self.domain}/nuclei/{severity}/{template}_{file_name}"
                self.run_template(template, output_file)