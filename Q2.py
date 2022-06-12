#2
a = int(input())
if a<120:
    print("Summer months:",a*2.10)
    print("Non-Summer months:",a*2.10)
elif 121<a<330:
    print("Summer months:",a*3.02)
    print("Non-Summer months:",a*2.68)
elif 331<a<500:
    print("Summer months:",a*4.39)
    print("Non-Summer months:",a*3.61)
elif 501<a<700:
    print("Summer months:",a*4.97)
    print("Non-Summer months:",a*4.01)
elif a>701:
    print("Summer months:",a*5.63)
    print("Non-Summer months:",a*4.50)