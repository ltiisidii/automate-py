import subprocess
from pathlib import Path

domain = input('Enter the domain name: ')


# Directories
create_assets= "results"
resultdir= create_assets + "/" + domain
subs=resultdir + "/subdomains"
print('[+] Create directories')
Path(create_assets).mkdir(parents=True, exist_ok=True)
Path(resultdir).mkdir(parents=True, exist_ok=True)
Path(subs).mkdir(parents=True, exist_ok=True)


# Subdomains
print('[+] Execting subdomains')

print('[+] 1- Running subfinder')
subprocess.call(f'subfinder -d' + ' ' + domain + ' ' + '-all -o ' + subs + '/subfinder.txt'
                , shell=True)

print('[+] 2- Running amass')
subprocess.call(f'amass enum -passive -d' + ' ' + domain + ' ' + '-o' + subs + '/amassp.txt'
                , shell=True)

print('[+] Combining and sorting subdomains')
subprocess.call(f'cat' + subs + '/*.txt | sort -u >' + ' ' + subs + '/subdomains.txt'
                , shell=True)

# Alive hosts
print('[+] Getting alive hosts')

subprocess.call(f'httpx -l' + ' ' + subs + '/subdomains.txt' + ' ' + '-silent -threads 9000 -timeout 30 | anew' + ' ' + subs + '/hosts.txt'
                , shell=True)
