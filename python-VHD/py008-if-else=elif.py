# 86 True False yapilari

sinir1=5000

sinir==4000 # mi derseniz False olarak doner

# 87 if  yapilari

sinir = 50000
gelir = 60000

gelir < sinir

if gelir<sinir:
    print("Geliriniz sinirdan kucuk")
    print(gelir*2)

if gelir>sinir:
    print("Geliriniz sinirdan buyuk")
    print(gelir*2)

 # Else yapisi
sinir = 50000
gelir = 60000

if gelir > sinir:
    print("Geliriniz sinirdan buyuk")
else :
    print("Geliriniz sinirdan kucuk")

if gelir < sinir:
    print("Geliriniz sinirdan buyuk")
else :
    print("Geliriniz sinirdan kucuk degil")


#

sinir = 50000
gelir = 51000

if gelir == sinir:
    print("Geliriniz sinir a esittir ")
else :
    print("Geliriniz sinir a esit degildir")


# 89 elif

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > sinir:
    print("Tebrikler , hediye kazandiniz")
elif gelir1 < sinir :
    print("Uyari!")
else :
    print("Geliriniz  esit ")

if gelir3 > sinir:
    print("Tebrikler , hediye kazandiniz")
elif gelir3 < sinir :
    print("Uyari!")
else :
    print("Geliriniz  esit ")

if gelir2 > sinir:
    print("Tebrikler , hediye kazandiniz")
elif gelir2 < sinir :
    print("Uyari!")
else :
    print("Geliriniz  esit ")

# 90 if ve input


sinir= 50000

magaza_adi = input("Magaza adini girin...: ")
gelir = int(input("GElirinizi girin ...: "))

if gelir > sinir:
    print("Tebrikler .."+magaza_adi+"  promosyon kazandiniz")
elif gelir < sinir:
    print(" Uyari ! Dusuk Gelir ..: "+str(gelir))
else:
    print("takibe devam")
