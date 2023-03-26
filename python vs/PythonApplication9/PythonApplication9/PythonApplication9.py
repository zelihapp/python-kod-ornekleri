# FOR DONGULERI(loop)

yorum_birakanlar = ["Isra Akdag" , "AAsaf Akdag","Zeliha Polat","Semra Polat","Zehra Polat","Hafide Akdag"]

for kullanici in yorum_birakanlar :
    print(kullanici) 


kullanici_sayisi = 0 
for kullanici in yorum_birakanlar :
    kullanici_sayisi = kullanici_sayisi + 1
    print(kullanici_sayisi , kullanici) 

#ad,soyad = yorum_birakanlar[0].split()[0] , yorum_birakanlar[0].split()[1]
#print(ad)
#print(soyad)

kullanici_sayisi = 0
for kullanici in yorum_birakanlar:
    kullanici_sayisi = kullanici_sayisi + 1 
    ad,soyad = kullanici.split()[0] , kullanici.split()[1]
    print("{0}. Kullanicinin Adi {1} ve Soyadi {2}".format(kullanici_sayisi , ad,soyad))



