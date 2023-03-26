# MAP , FILTER VE LAMBDA EXPRESSIONS

def karesini_al(x) :
    return x**2

print(karesini_al(5))

sayilar = [*range(1,6)]
print(sayilar)
for index in range(len(sayilar)) :                 # map kullanmiyor olsaydik
    sayilar[index] = karesini_al(sayilar[index])   # 5 sayinin degiskenlerini almak icin lenght
print(sayilar)

rakamlar = [*range(1,11)]
print(list(map(karesini_al, rakamlar)))            # map objesi olusuyor fakat liste icine alinmadan calismiyor veya ekrana basmiyor

def cift_sayilari_filtrele(x) :
    if x % 2== 0 :
        return x
    else :                                         # else kismini yazmasak da olur ayni islevi goruyor yazdigimizda da 
        return None 
print(cift_sayilari_filtrele(5))                   # filter kullanmiyor olsaydik

def tek_sayilari_filtrele(y) :                     # Daha profesyonel bir yazim.
    return y if y % 2 != 0 else None 
print(tek_sayilari_filtrele(5))

# return none ; hicligi dondururuyor ,hic bir sey dondurme 

sayilar1 = [*range(1,9)]
print(list(filter(cift_sayilari_filtrele , sayilar1)))  

# filter objesi olusuyor fakat liste icine alinmadan okunmuyor (ekrana yazmiyor)

print(list(map(lambda sayi : sayi ** 2 , sayilar )))   # fonksiyon cagirmadan lambda ile map kullanimi
                                                       # degisken , yapilmasi gereken islem return almadan , liste 


print(list(filter(lambda x : x if x%2==0 else None , sayilar))) # fonksiyon cagirmadan lambda ile filter kullanimi 
