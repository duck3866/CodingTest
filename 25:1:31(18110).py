import sys
def roundUp(num):
    if num - int(num) >= 0.5:
        return int(num)+1
    else:
        return int(num)
N = int(input())
arr = []
newArr = []
TrimmedAverage = roundUp(N * 0.15)
if N == 0:
    print(0)
else:
    for i in range(N):
        arr.append(int(input()))
    arr.sort()
    for i in range(TrimmedAverage,len(arr)-TrimmedAverage):
        newArr.append(arr[i])
    if len(newArr) != 0:
        print(roundUp(sum(newArr)/len(newArr)))
    else:
        print(0)
#    TrimmedAverage = roundUp(N * 0.15)
#    trimmed_arr = arr[TrimmedAverage:N-TrimmedAverage]
#    파이썬의 반올림이 사사오입 인지 오사오입인지 알게됨