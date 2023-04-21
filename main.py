from lib.subdomains import Subdomains
from lib.screenshots import ScreenshotCapture
from lib.nuclei import Nuclei

if __name__ == "__main__":
    domain = input('Enter the domain name: ')
    
    subdomains = Subdomains(domain)
    subdomains.run()

    screenshotcapture = ScreenshotCapture(domain)
    screenshotcapture.run()

    subdomains_obj = Subdomains(domain)
    nuclei = Nuclei(domain, subdomains_obj=subdomains_obj)
    nuclei.run_template("cves", "cves.txt")
    nuclei.run_template("dns", "dns.txt")
    nuclei.run_template("files", "files.txt")
    nuclei.run_template("panels", "panels.txt")
    nuclei.run_template("security-misconfiguration", "security-misconfiguration.txt")
    nuclei.run_template("subdomain-takeover", "subdomain-takeover.txt")
    nuclei.run_template("technologies", "technologies.txt")
    nuclei.run_template("tokens", "tokens.txt")
    nuclei.run_template("vulnerabilities", "vulnerabilities.txt")