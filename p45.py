dict1 = {}
a = int(input("請輸入n值："))
for i in range (1,a+1):
    b=input("請輸入獎牌種類：")
    c=input("請輸入獎牌數量：")
    dict1[b] = c
item1 = list(dict1.items())
for n1, n2 in item1:
    print("%s牌得到 %s 面" %(n1,n2))