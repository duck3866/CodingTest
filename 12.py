a = int(input())
b = 1

arr=[0 for i in range(a)]

for i in range(1,a+1):
    b=i
    for j in range(1,a+1):
        print('%d'%b,end=' ')
        b+=a
    print()