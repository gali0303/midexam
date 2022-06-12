a = int(input("輸入筆數n<4:"))
list1 = []
for i in range(a):
    b = input("輸入獎牌:").split()
    list1.append(b)
for j in list1:
    print(f'{j[0]}牌得到{j[1]}面')

