a= input("輸入一整數序列為:").split(" ")
list=[]
for i in range(len(a)):
    c=a.count((a[i]))
    list.append(c)
m=max(list)
if m>(len(a)/2):    
    a = list.index(m)
    print("過半元素為:"+a[a])
else:
    print("過半元素為:NO")