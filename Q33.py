ch = int(input("國文："))
en = int(input("英文："))
math = int(input("微積分："))
pe = int(input("體育："))
py = int(input("程式設計"))
score1 = {ch:"國文",en:"英文",py:"程式設計",pe:"體育",math:"微積分"}
avg = (ch + en + py + pe + math)/5
print("平均分數：",avg)
score = [ch,en,py,pe,math]
score.sort()
score.reverse()
max = score1[score[0]]
print("最高分科目：",max,score[0],"分")
score.reverse()
min = score1[score[0]]
print("最低分科目：",min,score[0],"分")
