a=input("請輸入正整數:")
b=[2]
for i in range(3,int(a)+1):
    test=True
    for j in range(len(b)):
        if i%b[j]==0:
            test=False
            break
        if (b[j]**2)>i:
            break
    if test:
        b.append(i)

list1=[]
for i in range(len(a)):
    for j in range(i,len(a)):
        data=a[i:j+1]
        if int(data) in b:
            list1.append(int(data))
s=len(list1)
if len(list1)==0:
    print("No prime found")
else:
    print("子字串中最大的質數值為:",max(list1))