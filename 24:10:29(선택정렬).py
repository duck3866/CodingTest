arr = list(map(int,input().split()))
for i in range(0,len(arr)-1,1):
    first = arr[i] #처음 숫자 저장
    min = 100 #가장 작은 수 찾기
    num = 0 #작은 수 찾기
    for j in range(i+1,len(arr),1):
        if arr[j] < min:
            min = arr[j]
            num = j
    if arr[i] > arr[num]:
        arr[i] = min
        arr[num] = first
    print(arr)