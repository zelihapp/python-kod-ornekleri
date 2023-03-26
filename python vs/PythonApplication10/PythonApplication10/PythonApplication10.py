# diger iterable objelerde for donguleri 

tupl = (1,3,5,7)
for sayi in tupl:
    print(sayi)

liste = [[1,2,],[3,4]]
for sayi1,sayi2 in liste :
    print(sayi1)

# sayi1 ilk haneye gelen degerler oluyor yani sayi1 = 1,3
# eger listenin icerisinde sayi1 ve sayi2 gibi iki eleman almak istiyorsak aldigimiz eleman sayisi listenin icindeki objelerle esit uzunlukta olmali
# yani 3 haneli bir alt liste varsa yazdirmak istedigimiz eleman sayisi da uc olmali 

liste1 = [[4,5],[6,7],[8,9]]
for x,y in liste1 :
    print(y)
# ic ice listede 3 ayri liste var ve bu listelerin icindeki eleman sayisi ile alinmak istenen eleman sayisi esit 

liste2 = [[10,1],[2,30],[6,7]]
for k,m in liste2 :
    print(k*m)


kullanici1 = {
    'ad' : 'naz' ,
    'soyad' : 'yaman'
}
print(kullanici1.items())

for key,value in kullanici1.items() :
    print("Key : {} \t Value :  {}".format(key,value))

for key in kullanici1.keys() :
    print("key : {}".format(key))





 