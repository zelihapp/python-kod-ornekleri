# FONKSIYONLAR KONU CALISMASI 

# durum ne olursa olsun her zaman ekrana 5 bastir

def bes_bastir() :   # basit bir fonksiyon oldugu icin parantez icine herhnagi bir arguman almadi 
    print(5)       
  
#  direkt yazdirmiyor . bu fonksiyonu her zaman cagiracagimizin garantisini tarayiciya vermiyoruz dolayisiyla
#  bu komutun yapmasini istedigimiz seyi ekrana dondurmesini istedigimiiz zaman yukarda olusturdugumuz fonksiyon ismini (bes_bastir)
#  yazdigimizda kod calisir hale geliyor

bes_bastir() 

# bir fonksiyonu calistirmak icin yapilmasi gereken sey fonksiyon isme ve sonrasinda parantez ve icine gelecek olan argumanlari eklemektir.

def alti_bastir():
    """
    Docstring : kodun calismasinda her hangi bir etki yok bir nevi aciklama satiri fonksiyonun ne yaptigini tanitmak icin kullanilir 
    örnegin: 
    arguman1 : int :
    return: string: rakamin string karsiligi
    """
    print(6)


# print ekrana bir sey yazdirir , return ekrana bir sey dondurur 
def bes_dondur() :
    return 5

bes_dondur() 

a = bes_bastir()  # besi yazar
print(a)           # ekrana none yazar. yoklugu donduruyor olacakti 

b = bes_dondur() 
print(b)         # dersek ekrana 5 yazar

# FONKSIYONLARDA ARGUMANLAR 

def sayi_dondur(sayi) :
    return sayi

sayi_dondur(10) # parantez icine ne yazilirsa onu geri dondurur

# DEFAULT ARGÜMANI

def rakam_dondur(rakam=250):
    return rakam

rakam_dondur(89)  # denilirse ekrana 89 yazar
 
# default argumani aksi iddia edilmezse hangi sayiyi vermissek onu dondurur

rakam_dondur()  # 250

def buyuk_sayiyi_dondur(a,b) :
    if a>b :
        return a
    elif b>a :
        return b

# eger fonksiyon icinde birden fazla return varsa fonksiyon calistirilirken ilk gorulen return a gore islem yapilir digerleri aktive olmaz
# sartli sorgulama haric bir den cok return kullanirken dikkatet !!!
