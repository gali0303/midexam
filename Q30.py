#30
ans = str(input())
while True:
    qua = str(input())
    if qua == "0000":
        break
    else:
        a = 0
        b = 0
        for i in qua:
            for t in ans:
                if i==t and qua.index(i)==ans.index(t):
                    a+=1
                elif i==t:
                    b+=1
        print(a,"A",b,"B")



