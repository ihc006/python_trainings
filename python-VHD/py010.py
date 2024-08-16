# 94 Break ve Continue

maaslar1=[8000,2000,5000,1000,7000,9000,3000]

dir(maaslar1)
maaslar1.sort()

maaslar1

for i in maaslar1:
    if i == 3000:
        print("kesildi")
        break                        # ic kontrol 3000 e geldiginde dongu duruyor donguden cikiliyo
    print(i)

for i in maaslar1:
    if i == 3000:
        continue    # ic ontrol 3000 i gordugunde devam eder ve onu atlamis olur
    print(i)
