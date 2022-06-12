ans = ['red','blue','red','green']
for j in range(10):#只能執行10次 10次後失敗
    a = input().split()#輸入答案 以空白間隔
    b = ''#設定一個空白值
    for i in range(4):#執行4次
        if a[i] in ans:
            if a[i]==ans[i]:
                b+='1'
            else:
                b+='2'
        else:
            b+='3'
    if b =='1111': 
        break
    else:
        print(b)
if b =='1111':
    print("正確答案")
else:
    print("挑戰失敗")