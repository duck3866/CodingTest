n = int(input())
aArray = list(map(int,input().split()))
bArray = list(map(int,input().split()))
bArray.sort(reverse = True)
s = 0
for i in range(0,len(bArray)):
    s += bArray[i] * min(aArray)
    aArray.remove(min(aArray))
print(s)
