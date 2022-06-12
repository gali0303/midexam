#7
a,c= input("輸入月租費形式及通話時間：").split(',')
a1 = int(a)
c1 = int(c)
if a1 == 186:
    b = c1 * 0.09
    if b > 186:
        print("通話費為：",round(b*0.8))
    else:
        print("通話費為：",round(b*0.9))
elif a1 == 386:
    b = c1 * 0.08
    if b > 386:
        print("通話費為：",round(b*0.7))
    else:
        print("通話費為：",round(b*0.8))
elif a1 == 586:
    b = c1 * 0.07
    if b > 586:
        print("通話費為：",round(b*0.6))
    else:
        print("通話費為：",round(b*0.7))
elif a1 == 986:
    b = c1 * 0.06
    if b >986:
        print("通話費為：",round(b*0.5))
    else:
        print("通話費為：",round(b*0.6))
else:
    print("輸入錯誤")