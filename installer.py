import os, time, sys
os.system('clear')
os.system('sudo apt update -y && sudo apt upgrade -y') 
os.system('sudo apt install nodejs -y')
os.system('sudo apt install npm -y')
os.system('npm i fake-useragent')
os.system('npm i colors')
os.system('npm i request')
os.system('npm i node-cron')
os.system('npm i readline-sync')
os.system('npm i random-useragent')
os.system('npm i axios')
os.system('npm i hpack')
os.system('npm i user-agent')
os.system('npm i cheerio')
os.system('npm i socks')
os.system('npm i http2-wrapper')
os.system('npm i node-fetch node-fetch@2')
os.system('npm i ejs')
os.system('npm i express-session')
os.system('npm i express')
os.system('curl https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt -o https.txt')
time.sleep(1)
os.system('clear')
time.sleep(1)
time.sleep(1)
print('Starting Proxy Automotive')
time.sleep(1)
os.system('screen -dm python3 proxies.py')
time.sleep(5)
print('Fuck You ')
time.sleep(5)
print('Your Setup Finish ')
sys.exit()