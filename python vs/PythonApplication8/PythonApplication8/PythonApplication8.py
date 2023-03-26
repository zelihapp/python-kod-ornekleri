hava_durumu = input("hava durumunu giriniz: ")

if hava_durumu == 'yagisli' :
    print("Semsiyeni al")
elif hava_durumu == 'gunesli':
    print("bir sey alma")
else:
    print("atkini al")


yas = 16 

if yas > 18 :
    print("Banka karti alinabilir")
else:
    print("banka karti veli izni ile alinabilir")

liste = ['a','b','c']
hedef_harf = 'd'
if hedef_harf in liste :   # in ifadesi listelere ozgu bir kavramdir cunku listeler birden fazla deger icerirler 
    print("buldum")
else:
    liste.append(hedef_harf)
    print(liste)

    #print("mevcut degil")

liste2 = ['z','e','l','i','h']
hedef_harf2 = 'a'

if hedef_harf2 in liste2:
    print("liste icinde zaten var")
else:
    liste2.append(hedef_harf2)
    print("listeye eklendi")
    print("guncel liste {}".format(liste2))

liste3 = ['k','l','m']
hedef_harf3 = 'k'

if (hedef_harf3 in liste3) and (hedef_harf3 == liste3[0]) :
    print("buldum ve ilk harf konumunda")
elif hedef_harf3 in liste3 :
    print ("buldum ama ilk konumda degil")
else:
    liste3.append(hedef_harf3)
    print("listeye eklendi")
    print("guncel liste {}".format(liste3))





