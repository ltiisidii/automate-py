from lib.subdomains import Subdomains
from lib.ipdiscovery import IPDiscovery
from lib.hostdetection import HostDetection
from lib.screenshots import ScreenshotCapture
from lib.nuclei import Nuclei

if __name__ == "__main__":
    domain = input('Enter the domain name: ')
    
    subdomains = Subdomains(domain)
    subdomains.run()

    ipdiscovery = IPDiscovery(subdomains.subs+'/hosts.txt', subdomains.resultdir)
    ipdiscovery.run()

    hostdetection = HostDetection(subdomains.subs+'/hosts.txt', subdomains.resultdir)
    hostdetection.run()

    screenshotcapture = ScreenshotCapture(domain)
    screenshotcapture.run()

    nuclei = Nuclei(domain)
    nuclei.run_template()