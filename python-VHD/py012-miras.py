# 102 miras/ inheritance yapilari
from fileinput import filename


class  Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""



class  DataSs(Employees):            # class  DataSs(): ilk tanimli iken sonradan kalitim istenen eklenir
    def __init__(self):
        self.Programming = ""


class Marketing(Employees):     # Employees tanimi ile kalitimi saglanir
    def __init__(self):
        self.StroyTelling= ""


veribil1 = DataSs()
veribil1.Programming = "Python"    # class  DataSs():  iken sadece DataSs in programming ozelli[i gozukur
veribil1.Address                   # class  DataSs(Employees): ile Employees sinifinin ozellikleri de eklenir


mark1 = Marketing()
mark1.StroyTelling
mark1.Address




class  Employees_New():     # daha fonksiyonel tanimlamak icin
    def __init__(self,FirstName,LastName,Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address

ali = Employees_New("a","b","c")
ali.FirstName


# 103 Fonksiyonel programlamaya giris
#104 yan etk's'z fonksiyonlar = Pure Function
 # yan etki


 A = 9  # 3 iken degistirdik

 def impure_sum(b):
     return b+A
impure_sum(6)
 def pure_sum(a,b):
     return a+b

 impure_sum(6)  # disaridan degere bagli etkileniyor

pure_sum(5,9)

# 105 olumcul yan etkiler

import os
class LineCounter:
    def __init__ (self, filename):
        script_dir = os.getcwd()  # Script'in çalıştığı dizin
        file_path = os.path.join(script_dir, filename)

        try:
            self.file= open(filename,'r')
        except FileNotFoundError:
            print(f" Dosya bulunamadi: {file_path}")
            raise
        self.lines=[]
    def read(self):
        self.lines = []
        for line in self.file:
            self.lines.append(line)
    def count(self):
        return len(self.lines)

    def close(self):
        self.file.close()

lc = LineCounter('F:\PythonProjects\python_ihc\python-VHD\deneme.txt')   # F:\PythonProjects\python_ihc\python-VHD\deneme.txt
                                                                         # yazilana kadar dosya bulamama hatasi ile kar;ila;tik path ile calisti

print(lc.lines)
print(lc.count())


lc.read()

print(lc.lines)
print(lc.count())



# 105
# fonsiyon ile yapilmasi

def read(filename):
  with open(filename,'r') as f:
      return [line for line in f]

def count(lines):
    return len (lines)

example_lines = read('F:\PythonProjects\python_ihc\python-VHD\deneme.txt')
lines_count = count(example_lines)
lines_count
