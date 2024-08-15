# 91 For dongusu

ogrenci = ["ali","veli","isik","berk","can"]

ogrenci[0]

for i in ogrenci :
    print(i)

# 92 for devam

maaslar=[100,200,300,400,500,600]

maaslar[0]

for i in maaslar :
    print(i)

# dongu ve fonksiyonlari birlikte kullanimi

def kare_al(x):
    print(x**2)

kare_al(2)

for i in maaslar:
    print(i)

   # maaslara %20 zam ile ilgili senaryo

maaslarp[0]*20/100+maaslar[0]

maaslar[0]*1.2

for i in maaslar:
    print(i*1.2)

def yeni_maas(x):
    print(x)
yeni_maas(4)

def yeni_maas1(x):
    print(x*1.2)

yeni_maas1(400)

for i in maaslar:
    yeni_maas1(i)
# 94 if for ve fonksiyon Kullanimi
# ornek senaryo  maaslari 300 0 altina %20 ustune %10 zam

maaslar1=[1000,2000,3000,4000,5000,6000]
def maas_ust(x):
    print(x*1.1)
def maas_alt(x):
    print(x * 1.2)

for i in maaslar1:
       print(i)

for i in maaslar1:
    if i>=3000:
        maas_ust(i)
    else:
        maas_alt(i)
