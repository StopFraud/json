import requests, random,json,re,pytz
from urllib.parse import unquote
from phone_gen import PhoneNumber
from transliterate import translit, get_available_language_codes

url = 'https://raw.githubusercontent.com/StopFraud/metadata/main/phrases.txt'
r = requests.get(url, allow_redirects=True)
open('phrases.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/StopFraud/metadata/main/cryptolist.txt'
r = requests.get(url, allow_redirects=True)
open('cryptolist.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/StopFraud/metadata/main/coin.txt'
r = requests.get(url, allow_redirects=True)
open('coin.txt', 'wb').write(r.content) 

url = 'https://raw.githubusercontent.com/StopFraud/metadata/main/names_f.txt'
r = requests.get(url, allow_redirects=True)
open('names_f.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/StopFraud/metadata/main/countries.txt'
r = requests.get(url, allow_redirects=True)
open('countries.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/StopFraud/metadata/main/surnames_f.txt'
r = requests.get(url, allow_redirects=True)
open('surnames_f.txt', 'wb').write(r.content)

url = 'https://www.mit.edu/~ecprice/wordlist.10000'
r = requests.get(url, allow_redirects=True)
open('wordlist10000.txt', 'wb').write(r.content)

with open('phrases.txt', 'r',encoding="utf-8") as file:
    data = file.readlines()
    
with open('coin.txt', 'r',encoding="utf-8") as file:
    coins = file.readlines()

with open('names_f.txt', 'r',encoding="utf-8") as file:
    names = file.readlines()

with open('surnames_f.txt', 'r',encoding="utf-8") as file:
    surnames = file.readlines()

with open('countries.txt', 'r',encoding="utf-8") as file:
    countries = file.readlines()

with open('wordlist10000.txt', 'r',encoding="utf-8") as file:
    wordlist10000 = file.readlines()


with open('phrases.txt', 'r',encoding="utf-8") as file:
    phrases = file.readlines()

with open('cryptolist.txt', 'r',encoding="utf-8") as file:
    cryptolist = file.readlines()


domains=['mail.ru','yandex.ru', 'rambler.ru', 'outlook.com', 'gmail.com', 'hotmail.com', 'list.ru', 'bk.ru', 'inbox.ru', 'internet.ru',\
'yahoo.com', 'aol.com', 'e1.ru','inbox.lv', 'dino.lv','human.lv', 'fit.lv','sok.lv', 'eclub.lv', 'zohomail.com', 'protonmail.com', 'mail.com',\
'mail.ru','yandex.ru', 'rambler.ru', 'outlook.com', 'gmail.com', 'hotmail.com','yahoo.com',\
 'cyberservices.com', 'protestant.com', 'ya.ru','box.az','byke.com','chez.com','email.ru','gmx.net','goldmail.ru',\
'sendmail.ru','sendmail.com','gold.az','mail.lv','mail.lt','tyt.by','mail.by','rambler.lv','rambler.cz','outlook.ru','tut.by',\
'mail.ru','yandex.ru', 'rambler.ru', 'outlook.com', 'gmail.com', 'hotmail.com','yahoo.com',\
'inet.ru','bigmailbox.com','lycos.com','netaddress.com','techemail.com','yandex.kz','yandex.lv','yandex.com','yandex.az','yandex.tr','ya.az',\
'mail.ru','yandex.ru', 'rambler.ru', 'outlook.com', 'gmail.com', 'hotmail.com','yahoo.com',\
'aport.ru','chat.ru','newmail.ru','sitek.net','zmail.ru','id.ru','ok.ru', 'ru.ru','icloud.com','thunderbird.net','yandex.com','zoho.com',\
'gmxmail.com','trustifi.com','mail.com','mailfence.com','outlook.ru','hotmail.ru','gmail.ru','fastmail.com','fastmail.ru','tutanota.com',\
'posteo.com','mailbox.org','mailbox.com','mailbox.ru','zohomail.ru','kolabnow.com','pochta.ru','post.ru']



def get_name():
    name=names[random.randint(1,len(names)-1)].replace('\n', '')
    return name

def get_surname():
    surname=surnames[random.randint(1,len(surnames)-1)].replace('\n', '')
    return surname

def get_final_name():
    name=names[random.randint(1,len(names)-1)].replace('\n', '')
    surname=surnames[random.randint(1,len(surnames)-1)].replace('\n', '')
    dice=random.choice([1,2,3])
#    _log (dice)
    if (dice==1):
        final_name=name
    if (dice==2):
        final_name=name+" "+surname
    if (dice==3):
        final_name=surname+" "+name
    return final_name

def get_final_name_from_name_surname(name, surname):
    dice=random.choice([1,2,3])
#    _log (dice)
    if (dice==1):
        final_name=name
    if (dice==2):
        final_name=name+" "+surname
    if (dice==3):
        final_name=surname+" "+name
    return final_name



def get_phone_full(country):
#    country=countries[random.randint(1,len(countries)-1)].replace('\n', '')
#    _log(country)

    #phone # depends on conutry
    ph=PhoneNumber(country)

    tn2=ph.get_number(full=True)
    phone_full=ph.get_number()
    return phone_full

def get_phone_short(country):
#    country=countries[random.randint(1,len(countries)-1)].replace('\n', '')
#    _log(country)

    #phone # depends on conutry
    ph=PhoneNumber(country)

    tn2=ph.get_number(full=False)
    phone_short=ph.get_number()
    return tn2



def get_email():
    domain=random.choice(domains)
    password=""
    for i in range (1,7):
        password=password+random.choice('01234567890')
    username=translit(final_name, reversed=True).replace(" ", "_").replace("'","").lower()+password
    email=username+"@"+domain
    return email

def get_email_from_final_name(final_name):
    domain=random.choice(domains)
    password=""
    for i in range (1,random.randint(5,8)):
        password=password+random.choice('01234567890')
    word=random.choice(wordlist10000).replace("\n","")
    word2=random.choice(wordlist10000).replace("\n","")
    dice=random.choice([1,2,3,4])
    if (dice==1):
        username=translit(final_name, reversed=True).replace(" ", "_").replace("'","").lower()+password
    if (dice==2):
        username=(word+word2).replace(" ", "_").replace("'","").lower()+password
    if (dice==3):
        username=(word+translit(final_name, reversed=True)).replace(" ", "_").replace("'","").lower()+password
    if (dice==4):
        username=(translit(final_name, reversed=True)+word).replace(" ", "_").replace("'","").lower()+password
    email=username+"@"+domain

    return email



def get_password():
    password=random.choice(['A','B','C','D','E','F','G','H'])
    for i in range (1,6):
        password=password+random.choice('abcdefghijklmnopqruvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range (1,4):
        password=password+random.choice('0123456789')
    password=password+'*'
    l = list(password)
    random.shuffle(l)
    password = ''.join(l)
    password=random.choice('abcdefghijklmnopqruvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+password
    return password


def get_phrase():
    phrase=phrases[random.randint(1,len(phrases)-1)].replace('\n', '')
    return phrase

def get_coin():
    coin="USDT wallet"
    crypto=cryptolist[random.randint(1,len(cryptolist)-1)].replace('\n', '')
    prefix=random.choice(['hi, I\'d like to get ', 'I was told to ask ', 'Requesting ', 'Provide ', 'Give me ', 'can you please arrange ', 'I need ', 'would you mind creating ', 'please create ', 'I want ', 'Friend told me to ask here for ', 'Request to create ', 'for this crypto: ', 'I am requesting ', 'Today I need '])
    suffix=random.choice(['wallet', 'account', 'wallet here', 'account here', 'coinbase wallet', 'investing wallet', 'brokerage account', 'trading account', 'crypto', 'Crypto', 'crypto wallet', 'cryptocurrency wallet'])
    dice=random.choice([1,2,3,4])
    if (dice == 1):
        coin=prefix+crypto+" "+suffix
    if (dice == 2):
        coin=coins[random.randint(1,len(coins)-1)].replace('\n', '')
    if (dice == 3):
        coin=prefix+crypto
    if (dice == 4):
        coin=crypto+" "+suffix


    return coin



def get_final_name(name, surname):
    dice=random.choice([1,2,3])
#    _log (dice)
    if (dice==1):
        final_name=name
    if (dice==2):
        final_name=name+" "+surname
    if (dice==3):
        final_name=surname+" "+name
    return final_name


def new_data(country_f):
    country_f=country_f.replace("\n","")
    name= get_name()
    surname=get_surname()
    final_name=get_final_name_from_name_surname(name, surname)
    phone_full=get_phone_full(country_f)
    phone_short=get_phone_short(country_f)
    email=get_email_from_final_name(final_name)
    password=get_password()
    final_name=get_final_name(name, surname)
    coin=get_coin()
#    email2=get_email()
    print(name,surname, final_name, phone_full,email)
   
    j={}
    j["name"]=name
    j["surname"]=surname
    j["final_name"]=final_name
    j["phone_full"]=phone_full
    j["phone_short"]=phone_short
    j["email"]=email
    j["password"]=password
    j["phrase"]=get_phrase()
    j["phrase2"]=get_phrase()
    j["answer"]=get_phrase()
    j["country_full_en"]=country_f
    j["coin"]=coin



#    country_f
#    print(co)
#    co='RU'
#    co=co.alpha_2
    j["country_alpha_2"]=str(names_alpha2[country_f])
    json_object = json.dumps(j, indent = 4) 
    print(json_object)
    return json_object


def ai(question):
    print("----AI start---")
#

    print("Q: "+question)
    a=[]
    #question='Здравствуйте, я создам запрос, с вами свяжется ваш менеджер.'
    words=question.replace(',','').replace('.','').replace('\n', '').lower().split()
    for word in words:
       if (len(word)>6):
           print (word)
           for d in data:
               if word in d.lower():
                   print(d)
                   a.append(d)

    if (len(a)>2):
        answer=random.choice(a)
    else:
        answer=random.choice(data)
    answer=answer.replace('\n', '')

    if (answer==question):
        answer=random.choice(data)

    dice=random.randint(1,10)
    if (dice==5):
        answer=random.choice(data)

    answer=answer.replace('\n', '')
    print(answer)
 


#    _log ("A: "+answer)
#    _log ("-----AI END--------")
    return (answer)





from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        country_r='Russia'
        if None != re.search('/api/country/*', self.path):
            country_r = str(self.path.split('/')[-1])
            print("country   "+country_r)
            if country_r=="random":
                country_r=random.choice(countries)
        answer=None
        if None != re.search('/api/ai/*', self.path):
            print("ai request")
            request_r = str(unquote(self.path.split('/')[-1]))
            answer=ai(request_r)
            

        json_object=new_data(country_r)
        if None != answer:
            j=json.loads(json_object)
            j["answer"]=answer
            json_object=json.dumps(j)
            print(json_object)
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json_object.encode())
#        self.wfile.write(json.dumps({
#            'method': self.command,
#            'path': self.path,
#            'real_path': parsed_path.query,
#            'query': parsed_path.query,
#            'request_version': self.request_version,
#            'protocol_version': self.protocol_version
#        }).encode())
        return

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        data = json.loads(post_body)

        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
#        self.wfile.write(jjencode())
#        self.wfile.write(json.dumps(j).encode())
#        self.wfile.write(json.dumps({
#            'method': self.command,
#            'path': self.path,
#            'real_path': parsed_path.query,
#            'query': parsed_path.query,
#            'request_version': self.request_version,
#            'protocol_version': self.protocol_version,
#            'body': data
#        }).encode())
        return

aplha2_names={}
names_alpha2={}
for key, val in pytz.country_names.items():
    print(key, '=', val, end=',')
    aplha2_names[key]=val
    names_alpha2[val]=key




if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), RequestHandler)
    print('Starting server at http://localhost:8000')
    server.serve_forever()
