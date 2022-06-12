ans = str(input("請輸入第一組數字："))
qua = str(input("請輸入第二組數字："))
a = 0
b = 0
for i in qua:
    for t in ans:
        if i == t and qua.index(i)==ans.index(t):
            a+=1
        elif i==t:
            b+=1
if a == len(ans):
    print(a,"A",b,"B","全對")
else:
    print(a,"A",b,"B","加油")