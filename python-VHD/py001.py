print("pycharm ile basladik bakalim")
#  Sayilar ve Stringler
# Basladik 002
# 31/07
"a" * 3
"a" + "b"
"a" + "-b"

a = 9
b = 10
a * b
# mvk="Sample text"
# del mvk
a1t = "Sample text"

len(a1t)

a1t.upper()

a1t.lower()

a1t.islower()
B=a1t.upper()
print(B)

a1t.isupper()
B=a1t.lower()
print(B)


# 01/08

# replace

texttest="gelecek guzel olacak"
texttest.replace("e","a")
texttest.replace("a","i")

# strip   bas ve sondaki

texttest=" gelecek guzel olacak  "
texttest.strip()  # ontanimli deger bosluk


texttest="*gelecek guzel olacak***"
texttest.strip("*")   # tanimli deger *


# bir komut la ilgili neler yapilabilir hangi komutlari da ogrenmeliyim vb de ise

# dir()  # komutu icine istenilen tip degisken yazilir calistirilir ki ilgili butun metodlar cikar

dir(texttest)
dir(str)

# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count',
# 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
# 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
# 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
# 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
