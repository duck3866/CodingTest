N,K = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
summ = 0
# 배열 A에서 작은 거 찾아서 배열 B에서 큰 거 찾아서 바꾸기
for i in range(K):
    max = 1000
    num1 = 0
    num2 = 0
    for j in range(len(arr1)):
        if arr1[j] < max:
            max = arr1[j]
            num1 = j
    min = 0
    for k in range(len(arr2)):
        if arr2[k] > min:
            min = arr2[k]
            num2 = k
    if max < min:
        arr1[num1] = min
        arr2[num2] = max
    if sum(arr1) > summ:
        summ = sum(arr1)
print(summ)
