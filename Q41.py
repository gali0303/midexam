a = int(input("搭了幾次電梯："))
b = [1]
for i in range(a):
    c = int(input())
    b.append(c)
total = 0
if b[0]>b[1]:
    total += ((b[0] - b[1])/1)*10
elif b[0]<b[1]:
    total += ((b[1] - b[0])/1)*20
if b[1]>b[2]:
    total += ((b[1] - b[2])/1)*10
elif b[1]<b[2]:
    total += ((b[2] - b[1])/1)*20
if b[2]>b[3]:
    total += ((b[2] - b[3])/1)*10
elif b[2]<b[3]:
    total += ((b[3] - b[2])/1)*20
if b[3]>b[4]:
    total += ((b[3] - b[4])/1)*10
elif b[4]<b[3]:
    total += ((b[4] - b[3])/1)*20
if b[4]>b[5]:
    total += ((b[4] - b[5])/1)*10
elif b[4]<b[5]:
    total += ((b[5] - b[4])/1)*20
print(int(total),"元")