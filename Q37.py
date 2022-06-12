n = int(input("整數n："))
if n<0 or n>1000000:
    print("輸入錯誤!")
a = []
while True :
    a.append(str(n))
    if n == 1 :
        break 
    elif n%2 != 0:
        n = int(3*n + 1)
    else:
        n = int(n/2)

b = " ".join(a)
print("數列：",b)

    
