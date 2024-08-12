# 67  tuple - demet  veri yapilari

t1=("ali","veli",1,2,3.4,[1,2,3,4,5])

t1="ali","veli",1,2,3.4,[1,2,3,4,5]


# tuple

t1=("eleman",)   # tek elemanli bir tuple olusturmak icin
type(t1)


####################################################
# Tuple Eleman islemleri
t2=("ali","veli",1,2,3,[1,2,3,4])

t2[1]

t2[0:3]

t2[2]=99   # degisiklik olmayacagina dair hata mesaji verir

# Dictionary= Sozluk      veri yapilari

sozlk={"Var1":"Python",
       "Ver1":"3.10",
       "Os1":"Windows 2022"}
sozlk

len(sozlk)  # goruldugu gibi burada 3 dger var.. sozluk tipinden dolayi

sozlk2= {"v1":10,
         "v2":20,
         "v3":30 }
sozlk2

sozlk3= {"v1": ["dev",10],
         "v2": ["vers",20,30],
         "v3": "Windows"}
sozlk3

# Sozluk eleman islemleri

sozlk3= {"v1": ["dev",10],
         "v2": ["vers",20,30],
         "v3": "Windows"}

sozlk3["v1"]
sozlk3["v2"]


sozlk4= {"v1": {"dev":10 , "os": 20},
         "v2": {"dev":10 , "os": 20},
         "v3": {"dev":10 , "os": 20}
         }
sozlk4

sozlk4["v1"]["os"]  # v1 deki os sozluk degerini verir


# Sozluk eleman ekleme ve cikarma
sozlk4= {"v1": {"dev":10 , "os": 20},
         "v2": {"dev":10 , "os": 20},
         "v3": {"dev":10 , "os": 20}
         }
sozlk4

sozlk4["v4"]= "dev"  # bir eleman ekledik

sozlk4['v1']= "v1 in yeni degeri"
sozlk4


sozlk4[5]="son eklenen deger"  # bir deger ekelem tarzi
sozlk4

liste1= [1,2,3,4,5]
liste1
