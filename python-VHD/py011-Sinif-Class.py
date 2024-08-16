# 97 Sinif / Class

class Verib():
    print("Sinif ilk denemsi")

# 98 sinif ozellikleri

class VeriBSpec():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []

VeriBSpec.bolum
VeriBSpec.bildigi_diller
VeriBSpec.sql # on tanimli deger gelir


VeriBSpec.sql='Hayir'

VeriBSpec.sql

# 99 sinif orneklemesi = instanation

ali = VeriBSpec()
ali.sql

ali.deneyim_yili

ali.bildigi_diller.append("Python")

veli=VeriBSpec()

veli.sql
veli.bildigi_diller

# 100 ornek ozellikleri

class verbl():              # budaki tanimlarin  isimleri ayni tanim ve self li tanillarin
    bildigi_diller=["R","Python"]
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []            # bu tarz kodlama ile her degiskenin icerigi kendine has
        self.bolum = ''

ali = verbl()
ali.bildigi_diller
 ali.bolum

veli = verbl()
veli.bildigi_diller

ali.bildigi_diller.append("python")
ali.bildigi_diller

veli.bildigi_diller
veli.bildigi_diller.append("java")
veli.bildigi_diller

verbl.bildigi_diller  # class in genel ozellikleri

verbl.bolum
ali.bolum = "isletme"
ali.bolum

veli.bolum
veli.bolum = "Kimya"

# 101  ornek metodlari


class veribl():              #
      calisanlar = []
      def __init__(self):
          self.bildigi_diller = []            # bu tarz kodlama ile her degiskenin icerigi kendine has
          self.bolum = ''
      def  dil_ekle (self,yeni_dil):           # bu kod ornegin 2 asamasinda yapildi
          self.bildigi_diller.append(yeni_dil)

ali= veribl()
ali.bolum
ali.bildigi_diller

veli= veribl()
veli.bolum
veli.bildigi_diller


dir(veribl)

veribl.dil_ekle   # hata alinir

ali.dil_ekle("R")
ali.bildigi_diller

veli.dil_ekle("python")
veli.bildigi_diller
