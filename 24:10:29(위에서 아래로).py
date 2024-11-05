n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in range(0,len(arr)-1,1):
    first = arr[i]
    next = arr[i+1]
    if first < next:
        arr[i] = next
        arr[i+1] = first
print(arr)