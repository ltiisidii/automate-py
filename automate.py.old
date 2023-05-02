import subprocess
from pathlib import Path

# Input
domain = input('Enter the domain name: ')

# Directories
create_assets= "results"
resultdir= create_assets + "/" + domain
subs=resultdir + "/subdomains"
screenshots=resultdir + "/screenshots"
nuclei=resultdir + "/nuclei"

# Custom Variables
hackerhandle= "hackerhandle" # Change this to your hacker handle

# Threads
gowitness_threads= "8" # Change this to the number of threads you want to use for gowitness
httpx_threads = "50" # Change this to the number of threads you want to use for httpx

# Rate limits
httpx_ratelimit=150
nuclei_ratelimit=150

# Timeouts
httpx_timeout=10 
amass_enum_timeout = 180

# lists
#resolvers=${tools}/resolvers.txt
# #resolvers_trusted=${tools}/resolvers_trusted.txt

# configs
amass_config= "~/.config/amass/config.ini"


# Create directories
print('[+] Create directories')
Path(create_assets).mkdir(parents=True, exist_ok=True)
Path(resultdir).mkdir(parents=True, exist_ok=True)
Path(subs).mkdir(parents=True, exist_ok=True)
Path(screenshots).mkdir(parents=True, exist_ok=True)
Path(nuclei).mkdir(parents=True, exist_ok=True)

# Subdomains
print('[+] Execting subdomains')

print('[+] 1- Running subfinder')
subprocess.call(f'subfinder -d' + ' ' + domain + ' ' + '-all -o ' + subs + '/subfinder.txt'
                , shell=True)

print('[+] 2- Running amass')
subprocess.call(f'amass enum -passive -d' + ' ' + domain + ' ' + amass_config + ' ' + '-timeout' + amass_enum_timeout + ' ' + '-o' + ' ' + subs + '/amassp.txt'
                , shell=True)

print('[+] Combining and sorting subdomains')
subprocess.call(f'cat' + ' ' + subs + '/*.txt | sort -u >' + ' ' + subs + '/subdomains.txt'
                , shell=True)


# Alive hosts
print('[+] Getting alive hosts')
subprocess.call(f'httpx -l' + ' ' + subs + '/subdomains.txt' + ' ' + '-silent -threads 9000 -timeout 30 | anew' + ' ' + subs + '/hosts.txt'
                , shell=True)


# Get IPs with dnsprobe
print('[+] Getting IPs')
subprocess.call(f'dnsx -l' + ' ' + subs + '/hosts.txt' + ' ' + '-o' + ' ' + subs + '/ips.txt'
                , shell=True)


# Get DNS takeover
#print('[+] Running Nuclei Template DNS Takeover Scan')
#subprocess.call(f'nuclei -l' + ' ' + subs + '/hosts.txt' + ' ' + '-t' + ' ' + 'dns-takeover' + ' ' + '-o' + ' ' + nuclei + '/dns-takeover.txt'
#                , shell=True)


# Get screenshots
print('[+] Getting screenshots')
subprocess.call(f'gowitness file -f' + ' ' + subs + '/hosts.txt' + ' ' + '--output' + ' ' + resultdir + '/screenshots' + ' ' + gowitness_threads + ' ' + '--disable-logging'              
                , shell=True)  


# Run Nuclei Templates
print('[+] Running Nuclei Templates')
#subprocess.call(f'nuclei' + ' ' + subs + '/hosts -t  -c 50 -H "x-bug-bounty:' + hackerhandle + ' ' + ' -o ' + nuclei + '/cve.txt
#subprocess.call(f'nuclei' + ' ' + subs + '/hosts -t  -c 50 -H "x-bug-bounty:' + ' ' + ' -o ' + nuclei + '/cve.txt
#                , shell=True)  


# Notifications to Telegram or Discord
print('[+] Sending notifications to Telegram or Discord')
