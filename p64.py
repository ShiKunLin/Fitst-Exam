a=int(input("請輸入第一個要判斷的數字："))
b=int(input("請輸入第二個要判斷的數字："))
c = a % 2
d = b % 2
if c == 0 or d == 0:
    print("N")
else:
    print("Y")
