import math
flag = False
m,n = map(str,input().split())#1,10
new_word = int(n+m)
m = int(m)
for i in range(2,int(math.sqrt(new_word))):
    if new_word % i == 0:
        flag = True

for j in range(2,int(math.sqrt(m))):
    if m % j == 0:
        flag = True
if flag != True:
    print("Yes")
else:
    print("No")
        
