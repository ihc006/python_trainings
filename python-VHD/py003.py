# veri yapilari
# lists

notlar=[90,80,70,60,50]

type(notlar)

liste=["a",19.3,90]

liste2=["a",19.3,90,notlar]

len(liste2)

type(liste2[0])

liste2[0]
liste2[1]
liste2[3]

tum_liste=[liste,liste2]

# del tum_liste   ....  adi gecen listeyi silmek icin

notlar2=[10,20,70,60,50]

notlar2[1]

notlar2[0:2]
# alt ve usteki ayni sonucu verir
notlar2[:2]

notlar3=[10,20,[70,60,50]]

# liste icindeki bir listenin elemanina ulasmak icin

notlar3[2][0] # listenin 2 elmani da lsite ve onun 0 inci elemani

# liste eleman ekleme degistirme silme islemleri


listen=["ali","veli","berkcan","ayse"]

listen

listen[1]="velinin_babasi"  # 1 nolu liste elemani atandi degistirildi

listen
listen[0:3]="alinin_babasi","velinin_babasi","berkin_babasi"  # listenin 3 elemanlarini dgistirmek icin

listen


# listeye yeni bir eleman eklemek icin

listen+["kemal"]  # gecici ekleme

listen

listen=listen+["kemal"]   # listen e yeni bir elemani kalici eklemek icin

listen

del listen[2]  # listede ki  ilgili bir elemani silmek icin

listen

#############################
# liste metodlari

listex=["ali","veli","ayse"]
dir(listex)   # liste ile ilgili metodlari gormek icin


# append & remove

listex.append("berkcan")
listex

listex.remove("berkcan")
listex


# 65. insert

listex1=["ali","veli","ayse"]
listex1

listex1.insert(0,"selim")   # 0 inci index e veri eklemek icin
listex1


listex1.insert(2,"kerim")

listex1

len(listex1)
listex1.insert(len(listex1),"beren")
listex1

# pop     listeden elemen silmek icin kullanilir


listex1

listex1.pop(0)

listex1

# 66 diger liste metodlari

listex2=["ali","veli","ayse","ali","veli","ayse","ali","veli","ayse","ayse"]

# count

listex2.count("ali")

listex2.count("ayse")

#copy

listex3=listex2.copy()

listex3

# extend

listex2.extend(["a","b",10])
listex2

# index

listex2.index("ali")

# reverse    listenin elemanlarini tersine cevirir

listex2.reverse()
listex2

# sort   listeyi kucukten buyuge siralar tipleri uygun olmali

listex4=[10,40,5,90]
listex4.sort()
listex4

# clear

listex4.clear()
listex4
