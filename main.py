from lib.subdomains import Subdomains
from lib.screenshots import ScreenshotCapture
from lib.nuclei import Nuclei

if __name__ == "__main__":
    domain = input('Enter the domain name: ')
    
    subdomains = Subdomains(domain)
    subdomains.run()

    screenshotcapture = ScreenshotCapture(domain)
    screenshotcapture.run()

#    nuclei = Nuclei(domain)
#    nuclei.run_template()