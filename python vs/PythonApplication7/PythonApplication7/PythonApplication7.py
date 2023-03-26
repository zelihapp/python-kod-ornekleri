# COK BOYUTLU VERI TIPI ( Dictionary )

dict1 = {'isim' : 'Zeliha', 'yas': 19 , 'lokasyon' : 'Berlin'}
print(dict1)

dict2 = {
    'isim' : 'Zeliha',
    'yas' : 19 ,              # ustteki yazim ile ayni ama okunulabilirlik acisindan daha cok tercih edilir 
    'dogdugu_sehir' : 'elazig',
    'yasadigi_sehir' : 'elazig'
}
print(dict2)


dict3 = {
    'isim' : 'Zeliha',
    'yas' : 19 ,
    'lokasyon' : {
        'dogdugu_sehir' : 'elazig',     # dictionary veri tipi ic ice kullanilabilir 
        'yasadigi_sehir' : 'elazig'
    }
}
print(dict3)


print(dict2['yas'])                # icindeki verilere ulasilir 

print(dict3['lokasyon'])

print(dict3['lokasyon']['yasadigi_sehir'])   #ic ice gecmis dictionary de ise verilere bu sekilde ulasilir 

print(dict2.get('yas'))                      # get metodu ile de dictionary icinden deger alinabilir 

print(dict2.keys())            # keys metodu anahtarlara karsilik gelir 

print(dict2.values())          # values metodu degerlere karsilik gelir 

print(dict2.items())           # her bir satiri tek tek yazar (items = anahtar ve deger metodu)


 





