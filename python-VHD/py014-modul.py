# 109 modul/paket /Kutuphane olusturmak

import HesapModulu as hm

hm.new_salary(1000)

hm.new_salary(2000)

from HesapModulu import new_salary

new_salary(4000)

print(str(hm.maaslar[0]))


# 110  dataa / istisnalar (exception)

a= 10
b= 0

a/b   # calistirildiginda division by zero hatasi alinir   Alinana hata sonrasi devam etmek icin


try:
    print(a/b)
except ZeroDivisionError:
    print("Payda da sifir olmaz")     # calisti program kirilmadi ve hatayi bize iletti



a=10
b="2"

a/b   # TypeError hatasi aldik

try:
    print(a/b)
except TypeError:
    print(" Tip hatasi var")
