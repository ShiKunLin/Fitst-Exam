a = int(input("組數為:"))
b = []
for i in range(a):
    c = input("第 %d 組:"%(i+1))
    b.append(int(c[0])*250+int(c[2])*175)
for i in range(a):
    print("第 %d 組應收費用:%d"%((i+1),b[i]))