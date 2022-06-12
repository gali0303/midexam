a = int(input("輸入n值"))
b = {}
for i in range(a):
    c = input("請輸入姓名:")
    d = input("請輸入電子郵件:")
    b[c]=d

e = input("請輸入要查詢電子郵件的姓名:")
print(e,"電子郵件帳號為",b[e])