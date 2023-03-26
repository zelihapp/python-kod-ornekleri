# KOLEKSIYON VERI TIPLERI ( List Ve Set )

liste = ['a','b','c','d','e','a']
print(liste)

liste = liste + ['f']   #koseli parantez olmazsa liste icine dahil etmez (ayni veri tipinde olmali)
print(liste)

print(liste[0]) 
print(liste[3:5])

liste.append('g')      #append listenin en sonuna ekleme yapar ve tekrardan atama gerektirmez
print(liste)

liste.pop()            #listenin son elemanini cikarir 
print(liste)
varpop = liste.pop()
print(varpop)

liste.pop(5)           # listeden cikarilmak istenen verinin index belirtip listeden pop ile cikartabiliriz 
print(liste)

sayilar = [123 , 234 , 456 , 345 , 867 , 678 , 1 , 1]
print(sayilar)
sayilar.sort()       # sort ifadesi kucukten buyuge siralama yapar 
print(sayilar)

sayilar.reverse()    # listeyi ters cevirir 
print(sayilar) 

print(set(sayilar))  # tekrar eden sayilar bir kez tek cagiriliyor ve listede koseli parantez ile cagirilan ifade artik suslu paranteze evriliyor 















