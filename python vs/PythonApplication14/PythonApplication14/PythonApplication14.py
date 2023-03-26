''' 
1 ile 100 arasinda rastgele uretilecek bir sayiyi asagi yukari ifadeleri ile buldurmaya calisin 
** "random modulu" icin "python random" seklinde arama yapin.
** 100 uzerinden puanlama yapin her soru 20 puan.
hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi uzerinden hesaplansin.
hak = 5
'''
import random
sayi = random.randint(1,10) # uygulama her calistiginda yeni bir sayi uretiyor
can = int(input("kac hak kulanmak istersiniz :"))
hak = can
sayac = 0

while hak > 0 :
    hak -= 1
    sayac += 1
    tahmin = int(input("tahmin: "))

    if sayi == tahmin :
        print(f"Tebrikler {sayac}. defa da bildiniz ! Toplam puaniniz: { 100 - (100/can)*(sayac-1) }")
        break

    elif sayi > tahmin :
        print("Yukari")

    else :
        print("Asagi")

    if hak == 0:

        print("hakkiniy bitti. tutulan sayi : {}".format(sayi))
 

