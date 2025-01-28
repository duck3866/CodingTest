T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    apate = [[0] * n for _ in range(k)] # 0 무조건 포함
    for i in range(n):
        apate[0][i] = i +1
    for j in range(1,k):
        for i in range(n):
            apate[j][i] = sum(apate[j-1][:i+1])
    print(sum(apate[k-1]))