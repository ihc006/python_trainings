# 84 degiskenler
x= 10
y=20   # global e ornek



def carpma_yap(x,y):
    return x*y

carpma_yap(2,3)   #  bu fonksiyonun icindekiler local degiskenlerdir disinda yokturlar

# local den Global i etkilemek


x = 10
y = 20
def carpma_yap2(x,y):
    return x*y

carpma_yap2(2,3)

x=[]

def eleman_ekle(y):
    x.append(y)

x.append(1)
x

x=[]

def eleman_ekle2(y):
    x.append(y)
    print(str(y)+" ifadesi eklendi")

eleman_ekle2("ali")
x
