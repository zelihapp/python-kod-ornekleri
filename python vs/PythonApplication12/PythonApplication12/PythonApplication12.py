# RANGE , ENUMERATE VE ZIP UYGULAMALARI 

# range 
print(type(range(10)))

print(list(range(10)))  # asagida verilen gosterimle ayni gorevde kullanilabilir 
print([*range(10)])     # no gosterime Broadcasting denir.

print(range(2,7))       # ikiden yediye kadar yazdirir
print(range(2,7,2))     # ikiden yediye kadar ikiser atlayarak yazdirir 

for sayi in range(10) :
    if sayi > 5 : 
        print(sayi)     # range icindeki her elemana for dongusu ile ulasabiliriz. 


# enumerate 

harfler = ['a','b','c','d','e']
for harf in enumerate(harfler) :  
    print(harf)
# enumerate hem elemanin kendisi hem de ona karsilik gelen indexin kendisini bastiriyor.
 

harfler1 = ['k','l','m','n','p']
for index, harf1 in enumerate(harfler1) :
    print("{}. harf: {}".format(index+1,harf1))
    # hem index hem de harfleri ayri ayri basma imkani da verebiliyor.

# zip 

# eleman sayisi esit olan iki listeyi birlestirir.

ulkeler = ['TR', 'FR' , 'DE']
siralama = range(1,4)

for ulke in zip(ulkeler,siralama) :
    print(ulke) 

# hem ulkeler listesinin hem de siralama listesinin uzunlugu 3tur birbirlerini esit oldugu icin zip kullanilabilir







