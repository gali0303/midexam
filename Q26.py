#26
while True:
    a = str(input("請輸入要檢測的字串："))
    if a == "end" or a == "結束":
        print("檢測結束")
        break
    else:
        b = input("檢測的單一字元：")
        list1 = a.count(b)
        print("字元",b,"出現次數",list1)
