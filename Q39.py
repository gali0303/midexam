a = int(input())
if a%2 == 0:
    for i in range(a):
        print(' '*(a-1-i)+'* '*(i+1))
    for i in range(a-1):
        print(' '*(1+i)+'* '*(a-1-i))
    print()
else:
    for i in range((a//2)+1):
        print(' '*(((a//2)+1)-i)+'*'*(2*i+1))
    for i in range(a//2):
        print(' '*(2+i)+'*'*((a-2)-(i*2)))
    print()
