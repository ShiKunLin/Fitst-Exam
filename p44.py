M=int(input("請輸入月份："))
D=int(input("請輸入日："))
S=(M*2+D)%3
if S == 0:
    print("普通")
elif S == 1:
    print("吉")
elif S == 2:
    print("大吉")