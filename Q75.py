b = []
while True:
    a = input("請輸入事項(若以無事項，請輸入end)：")
    if a == "end":
        break
    else:
        b.append(a)

for i in range(len(b)):
    print(str(i+1)+"."+b[i])
