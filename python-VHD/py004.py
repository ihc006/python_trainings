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
