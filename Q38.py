a = int(input())
b = []
for i in range(a):
    c = int(input())
    b.append(c)
d = []
for i in b:
    if i%9 == 0 or i%11 == 0:
        d.append(i)

for j in d:
    print("第",b.index(j)+1,"個點",j)
