# 72 Setler


s1= set()
s1

lst1=[1,"a","ali",123]  #liste
lst1
s2= set(lst1)
s2

tp1=("a","ali")  # tuple

s3=set(tp1)
s3

ali="her_sey_guzel_olacak"
type(ali)

s= set(ali)

veli=["ali","lutfen","ata","bakma","uzaya","git","git","ali","git","ali",]

s=set(veli)
s
len(s)
veli[0]  # liste deki 0 inci elemani verir

s[0]   # 'se tip hatasi verir

# 73 set elman ekleme cikarma

lst3=["Gelecegi","Yazanlar","kahramanlardir"]

lst3

s=set(lst3)

s

dir(s)

s.add("cesurlardir")

s

s.add("fedakarlarlardir")  # ekelnecek olani rastgele listeye ekler    {'Yazanlar', 'cesurlardir', 'Gelecegi', 'fedakarlarlardir', 'kahramanlardir'}


s.add("cesurlardir")   # ayni degeri eklemeye calistik ama eklemedi
s


s.remove("cesurlardir") # silmek istediginiz degeri
s


s.remove("cesurlardir") # silmek istediginiz degeri 2 'inci kez silmek istersek hata uzertir
s

s.discard("cesurlardir")  # s'lmek istedigi degeri arar bulamaz ise hatada vermez
s

############## Klasik m]me islemleri
