"""import random
kelimeler=["aslihan","karadeniz","seftali","böcek"]
sayilar=["07","0453","22"]


a=random.choice(kelimeler)+random.choice(sayilar)
print("kullanıcı adı:",a)"""

import random
kelimeler=[]
sayilar=[]
while True:
        kelime=input("lütfen kullanmak kelimeleri giriniz:")
        
        if kelime=="":
                break
        kelimeler.append(kelime)       
print(kelimeler)
while True:
                sayi=input("lütfen kullanmak istediğiniz sayıları  giriniz:")
                if sayi=="":
                        break
                sayilar.append(sayi)
print(sayilar)
rand=random.choice(kelimeler)+random.choice(sayilar)
print("kullanıcı adi:",rand)
a=random.choice(kelimeler)+random.choice(sayilar)
print("kullanıcı adı:",a)