# string ve char

strvar = "Python"
name = "ZELIHA"
print(strvar)
print(strvar[2])        # tek bir eleman alinir 
print(strvar[2:5])      # 2 ile 5 arasindaki elemanlari alir 
print(strvar[1:2:5])    # baslangic ve bitis arasindaki elemanlar ucuncu kisimdaki degere gore atlayarak degerler alinir 
print(strvar[:2])       # baslangictan itibaren 2 ye kadar olan elemanlari alir 
print(strvar[3:])       # 3 den son hanaye kadar olan elemanlari alir 
print(len(strvar))      # lenght(uzunluk) komutudur. kelimenin kac harften olustugunu bulmaya yarar
print(strvar.upper())   # kelimenin tum harflerini buyuk harfe cevirir 
print(name.lower())     # kelimenin tum harflerini kucuk harfe dondurur 

strvar = strvar + " ogren"
print(strvar)

print(strvar.split())      # python ve ogren arasindaki bosluk uzerinden bu ifadeyi iki tane elemana ayirir ve bir listenin icine ayrilan kelimeleri atiyor 
print(strvar.split("o"))   # belli bir karakter uzerinden elemanlara ayirir 



