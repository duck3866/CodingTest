a=int(input())
for i in range(1,a+1):
    if i**2 >= a:
        break
for j in range(1, a):
    if (i-1)**2==a-j:
        print(j, i-1)
        break