#11
a,b = input("輸入月及日：").split(" ")
b1 = int(b)
if a == "01":
    if b1>=21:
        print("星座為：Aquarius")
    else:
        print("星座為：Capricorn")
elif a == "02":
    if b1>=19:
        print("星座為：Pisces")
    else:
        print("星座為：Aquarius")
elif a == "03":
    if b1>=21:
        print("星座為：Aries")
    else:
        print("星座為：Pisces")
elif a == "04":
    if b1>=21:
        print("星座為：Taurus")
    else:
        print("星座為：Aries")
elif a == "05":
    if b1>=22:
        print("星座為：Germini")
    else:
        print("星座為：Taurus")
elif a == "06":
    if b1>=22:
        print("星座為：Cancer")
    else:
        print("星座為：Germini")
elif a == "07":
    if b1>=23:
        print("星座為：Leo")
    else:
        print("星座為：Cancer")
elif a == "08":
    if b1>=24:
        print("星座為：Virgo")
    else:
        print("星座為：Leo")
elif a == "09":
    if b1>=24:
        print("星座為：Libra")
    else:
        print("星座為：Virgo")
elif a == "10":
    if b1>=24:
        print("星座為：Scorpio")
    else:
        print("星座為：Libra")
elif a == "11":
    if b1>=23:
        print("星座為：Sagittarius")
    else:
        print("星座為：Scorpio")        
elif a == "12":
    if b1>=22:
        print("星座為：Capricorn")
    else:
        print("星座為：Sagittarius")