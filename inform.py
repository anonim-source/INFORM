
import requests
import json
import sys
from pyfiglet import Figlet
import time
from colorama import *


# Başlık
def index():
    f = Figlet(font='slant')
    print(Fore.GREEN + f.renderText('inform'))

# ip hakkında bilgi
def ip_info():
    print(Fore.YELLOW+"""
    [1]Kendi İpinizi Sorgulama
    [2]Hedef İp Sorgulama
    [3]Anasayfaya Dönme
    """)
    secim = input("Seciminizi Girin :")
    if secim == "1":
        rq = requests.get("https://ipinfo.io/?token=b48af843c01309")
        respon = rq.json()
        for a in respon:
            print(Fore.LIGHTMAGENTA_EX+a,respon[a], sep="= :")
        sec = input("cıktıyı kaydedelim mi (y/n) :")
        if sec == "y":
            dosya = open("kendiipim.txt","w")
            dos_k = dosya.write(str(respon))
            dosya.close()
            print(10*"-","kaydedildi",10*"-")
            return ip_info()
        else:
            return ip_info()
    elif secim == "2":    
        try:
            ip = str(input("ip adresini girin örnek(192.168.1.1):"))
            link = "https://ipinfo.io/"+ip+"?token=b48af843c01309"
            reques = requests.get(link)
            s = reques.status_code
            req = reques.json()
            for i in req:
                print(Fore.LIGHTCYAN_EX+i,req[i], sep="= :")
            sec = input("cıktıyı kaydedelim mi (y/n) :")
            if sec == "y":
                dosya = open(ip+".txt","w")
                dos_k = dosya.write(str(req))
                dosya.close()
                print(10*"-","kaydedildi",ip,10*"-")
                return index()
            else:
                return index()
        except:
            pass
    elif secim =="3":
        return index()
    else:
        print("Yanlış Tuşlama")
        return ip_info()
        
# Web sitedeki Dosyaları bulma
def websitede_dosya():
    try:

        link = input(str("site linkini girin örnek(exapmle.com):"))
        fuzz = open("dosyabulma.txt","r")
        fuzzread = fuzz.read()
        bulunanlar=[]
        try:
            for i in fuzzread.splitlines():
                attack = requests.get("https://"+link + "/" + i)
                respon = attack.status_code
                if respon ==200:
                    print("-"*30)
                    print(Fore.LIGHTGREEN_EX+"Bulundu >",i)
                    print(Fore.LIGHTGREEN_EX+"link >",attack.url)
                    print("-"*30)
                    bulunanlar.append(attack.url)
                else:
                    print(Fore.MAGENTA+"Bulunamadı >",i)
            for bul in bulunanlar:
                print("-"*30)
                print("Bulunanlar >", bul)
        except KeyboardInterrupt:
            return index()
    except:
        return index()
# sitelerin admin panelini bulma
def admin_panel():
    try:
        link = input("hedef link girin örnek(example.com) :")
        dosya = open("links.txt","r+")
        dosya_r = dosya.readlines()
        dosya.close()
        bulunan=[]
        try:
            for  i in dosya_r:
                request = requests.get("https://"+link + "/" + i)
                urladmin = request.url
                response = request.status_code
                if response == 200:
                    print("-"*30)
                    print(Fore.LIGHTGREEN_EX+"admin panel bulundu >",i)
                    print("link >",urladmin)
                    print("-"*30)
                    bulunan.append(urladmin)
                else:
                    print(Fore.MAGENTA+"bulunamadı >",i)
            for buladmin in bulunan:
                print("-"*30)
                print("Bulunanlar >", buladmin)  
        except KeyboardInterrupt:
            print("durdurdunuz")
    except:
        return index()


# Zararlı url sorgulama
def link_girme():
    print(Fore.CYAN+"NOT= zararlı bağlantılar USOM (Ulusal Siber Olaylara Müdahale Merkezi) websitesinden sorgulanıyor")
    link = input(Fore.WHITE+"örnek(zararlı.com)linki örnekteki gibi girin :")
    request = requests.get("https://www.usom.gov.tr/url-list.txt")
    statu = request.status_code
    response = request.text
    if link in response:
        print("-"*30)
        print("Zararlı link >",link)
        print("-"*30)
        print("Anasayfaya Yönlediriyorum")
        time.sleep(2)
        return index()
    else:
        print("-"*30)
        print(Fore.LIGHTGREEN_EX+"Zararlı Değil >",link)
        print("-"*30)
        print("Anasayfaya dönüyorsunuz")
        time.sleep(2)
        return index()

index()
# secım kısmı 
while True:
    print(Fore.RED+"""
    [1]İp Hakkında Bilgi
    [2]Web sitelerindeki Dosyaları Bulma
    [3]Admin Panel Bulma
    [4]Zararlı Bağlantı Tespiti
    [5]Sistemden cıkma
    """)
    secım = input(Fore.LIGHTWHITE_EX+"Seciminizi Girin :")
    if secım == "1":
        ip_info()
    elif secım == "2":
        websitede_dosya()
    elif secım == "3":
        admin_panel()
    elif secım == "4":
        link_girme()
    elif secım =="5":
        c = Figlet(font='slant')
        print(Fore.LIGHTYELLOW_EX+c.renderText('By By'))
        sys.exit()
    else:
        print("-"*10,"hatalı tuslama tekrar deneyin","-"*10)
        continue
