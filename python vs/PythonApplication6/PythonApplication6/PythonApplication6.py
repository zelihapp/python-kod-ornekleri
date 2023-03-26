# SABIT KOLEKSIYON VERI TIPI ( Tuple )  immutable = degistirilemez ifadelere verilen isim 

liste = ['a','b','c','d','e','a']
print(liste)
tup = ('a','b','c','d','e','a')
print(tup)

liste[0] = 12312
print(liste)

"""
tup[0] = 12312   
print(tup)
# boyle bir islem soz konusu olamaz tuple de elemanlar degistirelemez 
# indexlenebilir ama yeni deger atamasini desteklemez 
tup.index(true) -> hata verir (value error)
"""

print(tup.count('a')) # listede istenilen elemandan kac adet oldugunu sayar 

print(tup.index('b')) # verilen ifadenin index numarasini gosterir 
print(tup.index('a')) # ilk nereden verilmisse sadece o index numarasini dondurur







 





