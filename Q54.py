a = float(input("請輸入路程公里數(km):"))
if a <1.5:
    print("所需車資為：",75)
else:
    if (a-1.5)>0.25:
        if (a-1.5)%0.25 != 0:
            print("所需車資為：",int(75+(((a-1.5)//0.25)+1)*5))
        else:
            print("所需車資為：",int(75+((a-1.5)//0.25)*5))
    else:
        print("所需車資為：",80)