b = []
for i in range(0,10):
    a = int(input("請輸入第"+str(i+1)+"個數字："))
    b.append(a)

b.sort()
b.reverse()
print("最大的3個數字為：",b[0],",",b[1],",",b[2])
b.reverse()
print("最小的3個數字為：",b[0],",",b[1],",",b[2])