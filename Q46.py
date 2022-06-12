a= int(input("輸入筆數n：(n<4)"))
c = int(input("選擇方式(1.keys及values 2.items)"))
d1 ={}
d2 ={}
if c == 1:
    for i in range(a):
        d,e = input("輸入獎牌:").split()
        d1[d] = e
    for j in d1:
        print(f'{j}牌得到{d1[j]}面')
elif c == 2:
    for i in range(a):
        f,g = input("輸入獎牌:").split()
        d2[f] = g
    item1 = d2.items()
    for name,num in item1:
        print("%s牌得到 %s 面" % (name,num))

