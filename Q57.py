a,f = input("請選擇主餐及升級的套餐：").split()
b = input("是否升級大杯飲料：")
c = input("是否換成大薯：")
d = {"1":72,"2":62,"3":82,"4":44,"5":60}
e = {"A":55,"B":68}
if b == "是":
    if c == "是":
        print("總共為",d[a]+e[f]+7+13,"元")
    else:
        print("總共為",d[a]+e[f]+7,"元")
else:
    if c == "是":
        print("總共為",d[a]+e[f]+13,"元")
    else:
        print("總共為",d[a]+e[f],"元")
