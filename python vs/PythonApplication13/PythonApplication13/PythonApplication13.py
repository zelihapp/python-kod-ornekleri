# BREAK , CONTINUE VE PASS

# break 

harfler = ['a','b','c','d','e'] * 100  # bu listeden 100 tane var anlaminda 

for index,harf in enumerate(harfler) :
    # c harfinin hangi konumda tutuluyor ?
    if harf == 'c' :
        print("{} harfi {}. indexte ".format(harf,index)) 
        break  # break komutu donguye ait bir komut ve donguden cikmasi gerektigini soyluyor.

# continue

for sayi in range(1,6) :
    if sayi % 2 == 0 : #cift sayi sorgulama mantigi 
        continue       # devam et
    print(sayi)        # tek sayilari yazar 

# pass

for sayi in range(1,6) :
    if sayi % 2 == 0 :
        pass              
    else:
        print(sayi) 

if sayi < 5 :
    pass     # pass yazmadan bos birakirsak hata verir ama pass(orayi gec) ile hata vermeden atlar (kodun daha gelistirilemeyen bolumlerinde kullanimi var)
else :
    print(hey)



