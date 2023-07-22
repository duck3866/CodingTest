n = int(input())
cnt = 0
while True:
    if n % 5 == 0:
        cnt = n//5
        print(cnt)
        break
    n -= 3 
    cnt += 1 #여기까지는 내가 푼거
    if n < 0:
        print(-1)
        break