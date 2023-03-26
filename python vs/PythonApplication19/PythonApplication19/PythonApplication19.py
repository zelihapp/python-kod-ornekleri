# INPUT KOMUTU UZERINDEN KULLANICI GIRDISINI ONAYLAMAK

def sayi_girdisi_kontrol() : 
    girdi = input("Bir sayi giriniz: ")

    if girdi.isdigit() :                # isdigit komutu "sayi mi?" sorgusudur
        print("Tebrikler sayi tipi deger girdiniz")
    else :
        print("bu bir sayi tipi degisken degildir")

sayi_girdisi_kontrol()

# kullanici sayi tipinde deger girine kadar calisan program

def sayi_girdisi_kontrol_dongu() :
    girdi = input("Bir sayi giriniz: ")

    while not girdi.isdigit() :               # iki false trueya döndürür
        print("Bu bir sayi tipi degisken degildir")
        girdi = input("Bir sayi giriniz: ")

    else :
        print("tebrikler sayi tipinde deger girdiniz: ")

sayi_girdisi_kontrol_dongu() 

def eposta_kontrol() :

    giren = input("Gecerli bir e posta adresi giriniz: ")

    while not(('.' in giren) and ('@' in giren)) :
        print("bu gecerli bir e posta adresi degildir")
        giren = input("Gecerli bir e posta adresi giriniz: ")
    else :
        print("e-posta adresiniz ile basariyla giris yaptiniz...")

print(eposta_kontrol())



