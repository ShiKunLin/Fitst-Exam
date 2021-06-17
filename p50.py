a = input("剔除重復的字")
b=a.replace("，","")
c=b.replace("。","")
d=c.replace("？","")
list=[]
for i in range(0,len(d)):
    ct=0
    for j in d:
        if d[i]==j:
            ct+=1
    if ct>=2:
        list.append(d[i])
set(list)