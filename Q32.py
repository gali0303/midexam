a = int(input("小明身上有幾元?"))
b = int(input("販賣機有幾種飲料?"))
c = []
for i in range(b):
    d = int(input())
    c.append(d)

e = 0
for i in c:
    if a>=i:
        e += 1
    else:
        e = e

print(e)