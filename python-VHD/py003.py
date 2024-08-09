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


# insert
