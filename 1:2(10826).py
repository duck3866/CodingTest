n = int(input())
if n == 0 or n == 1:
    fibo = n
else:
    fibo_minus_2 = 0
    fibo_minus_1 = 1
    fibo = 0
    cnt = 2
    while cnt <= n:
        fibo = (fibo_minus_1 + fibo_minus_2)
        fibo_minus_2 = fibo_minus_1
        fibo_minus_1 = fibo
        cnt += 1
print(fibo)