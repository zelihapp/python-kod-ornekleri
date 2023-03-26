# TRY , EXCEPT VE FINALLY KOMUTLARI ILE HATA TEDBIRI 

# kodumuzu kursun gecirmez hala getirmek icin

# round(1.3) ->  yuvarlama komutu

def tam_sayiya_cevir() :
    girdi = input("Bir ondalik sayi giriniz: ")     # input ile girilen ifadeleri ilk olarak string olarak aliyor 

    print("Yuvarlama isleminin sonucu: {}".format(round(float(girdi))))

tam_sayiya_cevir()

def tam_sayiya_cevir2() :
    girdi = input("bir ondalik sayi giriniz : ")

    try :
        girdi = float(girdi) 
        print("yuvarlama isleminin sonucu : {}".format(round(girdi)))  # bu kismi else ile ayirip da yazmak mümkündür
    except : #calismadigi harici durumda 
        print("{} girdisi ondalik tipe cevrilemiyor".format(girdi))
     
tam_sayiya_cevir2() 

def tam_sayiya_cevir3() :
    girdi = input("bir ondalik sayi giriniz: ")

    status = " "
    try :
        girdi = float(girdi)
        print("yuvarlama isleminin sonucu: {}".format(round(girdi))) 
        status = "basarili"
    except : 
         print("{} girdisi ondalik tipe cevrilemiyor".format(girdi)) 
         status = "basarisiz"
    finally :
        print("Tam sayiya cevirma islemi {} olarak tamamlandi".format(status))
tam_sayiya_cevir3()

