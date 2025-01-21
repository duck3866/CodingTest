human = int(input())
size = list(map(int,input().split()))
Tclose, penBuy = input().split()
Tcnt = 0
for i in size:
    if i % int(Tclose) == 0:
        Tcnt += i//int(Tclose)
    else:
        Tcnt += (i//int(Tclose)) + 1
print(Tcnt)
package = human// int(penBuy)
print(package, human - (package * int(penBuy)))
    
