n,m = map(int,input().split())
one = []
package = []
for i in range(m):
    p,o = map(int,input().split())
    one.append(o)
    package.append(p)
one_price = min(one)
package_price = min(package)
onlyOne = one_price * n
cnt = 0
coin = 0
while(cnt < n):
    if(n - cnt > 6):
        coin += package_price
        cnt+= 6
    else:
        if(coin + (one_price * (n-cnt)) > 
           coin + package_price):
            coin += package_price
            cnt += 6
        else:
            coin += (one_price * (n - cnt))
            cnt += (n-cnt)
if(onlyOne > coin):
    print(coin)
else:
    print(onlyOne)
# 패키지 6개당 가격, 1개당 가격
#1. 개당 가격으로 전부 나눈거 하나
#2. 패키지랑 단일 
#3. 둘중에 더 싼거 고르기