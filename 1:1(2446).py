
a = int(input())
for i in range(a,0,-1):
    print(' '*(a-i)+'*'*(i+(i-1)))
for j in range(a-1,0,-1):
    print(' '*(j-1)+'*'*(((a-j)*2)+1))