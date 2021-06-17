a=int(input("請輸入一個正整數(限制10以下):"))
for i in range(1,a+1):
  for j in range(1,i+1):
    b=i*j
    print("%2d" %(b),end=" ")
  print()