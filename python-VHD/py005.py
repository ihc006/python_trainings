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

############## Klasik kume islemleri
# difference()   iki kumenin farki
# intersection()  iki kumenin kesisimi
# union()  iki kumenin birlesimi
# symmetric_difference()  ikisinde de olmayanlari


set1= set([1,2,3,4])
set2= set([1,3,5,6])
 set2
 set1
                               # difference ile - ayni sonuc alinir
 set1.difference(set2)           # 1 de olup 2 de olmayanlar
 {2, 4}

set2.difference(set1)           # 2 de olup 1 de olmayanlar
 {5, 6}


 set1-set2      # yukaridakiler ile ayni sonuclari aliriz
 set2-set1

 set1.symmetric_difference(set2)

 set1= set([1,2,3,4])
 set2= set([1,3,5,6])

 set1.intersection(set2)           # intersection ile & ayni sonuc alinir
 set1 & set2
 set2.intersection(set1)

 kes= set1 & set2            # intersection ile kesisim alinir

 kes

 birlesim= set1.union(set2)     # union ile iki kume birlesir
 birlesim

 set1.intersection_update(set2)
 set1    # set1 icerigi guncellendi

 set2

 # set lerde sorgu

 set3 = set([7,8,9,10])
 set4 = set([5,6,7,8,9,10,11])
 set3
 set4

 # iki kume bos mu

 set3.isdisjoint(set4)          # false donerse ki oyle oldu  kesisimleri bos kume degil   true donse idi bos kume olacakti
 set4.isdisjoint(set3)

set3.issubset(set4)               # .subset() true/false bir kumenin elemanlarinin baska bir kume icinde yer alip almadigi

set4.issuperset(set3)              # bir kumenin digerini kapsayip kapsamadigi
