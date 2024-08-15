# 77 Fonksiyonlar

print()   # cikti yok

print     # hata mesajinda foksiyon oldugu yazili

?print    # ? ile fonksiyonun detaylari gelir

len("a")

# fonksiyon yazma

# kare ifadesi icin a**2 ... anin 2 inci dereceden kuvveti
3**2  # 3 un karesi 2 dereceden kuvveti

3**3 # 3 un 3 uncu dereceden kuvveti


def kareal(x):
     print(x**2)

kareal(5)

# bilgi notuyla cikti uretmek

def kareal(x):
    print("Girilen sayinin karesii..: "+str(x ** 2))  # str () ile x**2 ifadesi yazilmaz ise str ile int birlestirme hatasi aliniz


kareal(9)

def kareal(x):
    print("Girilen sayi..: "+str(x)+" nin karesii..: "+str(x ** 2))

    kareal(9)

# 80 iki argumanli fonksiyon tanimlama
..

def carpmayap(x,y):
    print("Girilen sayilar..: "+str(x) +" ve "+str(y) +" nin carpimlari .: "+str(x * y))

carpmayap(15,24)


# on tanimli argumanlar

def carpmayap2(x,y=15):
    print("Girilen sayilar..: "+str(x) +" ve "+str(y) +" nin carpimlari .: "+str(x * y))



carpmayap2(35)  # eger ikinci deger yazilmaz ise on tanimli degeri alir

carpmayap2(35,4)   # 2 inci deger girilir ise onu alir
