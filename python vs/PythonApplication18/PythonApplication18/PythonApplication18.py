# INPUT KOMUTU

input("Bir sayi giriniz: ")

girdi = input("bir sayi giriniz: ")
print(type(girdi))                  # str
print(type(int(girdi)))             # kullanicidan alinan verinin cevrilebilmesi gerekiyor 

def uygulama() :
    girdi = input("bir rakam giriniz: ")
    islem = input("Verinin tek mi cift mi oldugunu sorgula: ")

    if islem == "cift":
        if int(girdi) % 2 == 0:
            return "evet, {} sayisi bir cift sayidir".format(girdi)
        else :
            return "hayir, {} sayisi cift sayi degildir".format(girdi)

    elif islem == "tek":
        if int(girdi) % 2 != 0 :
            return "evet, {} bir tek sayidir".format(girdi)
        else :
            return "hayir, {} bir tek sayi degildir".format(girdi)

print(uygulama())





