'''
Soru : girilen bir sayinin asal olup olmadigini bulun.
**Asal Sayi 1 ve kendisi haric tam boleni olmayan sayilara denir
'''

sayi = int(input("sayi: "))
asalmi = True

if sayi == 1 :
   asalmi = False

for i in range(2,sayi) :
    if ( sayi % 2 == 0) :
        asalmi = False
        break

if asalmi:
    print("Sayi asaldir")
else: 
    print("Sayi asal degildir")


