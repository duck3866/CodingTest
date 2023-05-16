a=int(input())
b= a // 2
for i in range(1,a+1,2):
    for j in range(1):
        print(' '*b+'*'*i,end='')
    b-=1
    print()