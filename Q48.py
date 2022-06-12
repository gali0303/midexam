a = int(input("輸入筆數n:"))
dict1 = {}
for i in range(a):
    b,c = input().split()
    dict1[b] = c
d = str(input("輸入欲查詢的單字:"))
if d in dict1:
    print(d+"中文意思為"+dict1[d])
else:    
    print("字典未有此單字")
