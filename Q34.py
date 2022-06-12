a = int(input("輸入一正整數(11<=n<=1000)："))
if a<11 or a>1000:
    print("輸入錯誤!")
if a%2 == 0 and a%11 == 0:
    if a%5 != 0 and a%7 != 0:
        print(a,"為新公倍數?","Yes")
    else:
        print(a,"為新公倍數?","No")
else:
    print(a,"為新公倍數?：","No")