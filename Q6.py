#6
a = input("輸入值為：(1~7個數值)").split(",")
l = sorted(a)
b = sorted(a,reverse=True)
i = "".join(l)
min = int(i)
a = "".join(b)
max = int(a)
ans = max-min
print("最大值數列與最小值數列差值為：",ans)

