def BinarySearch(target, a):
    left = 0
    right = len(a)-1
    # print("타겟:중간값",target,middle)
    while left <= right:
        middle = (left + right)//2
        if a[middle] == target:
            return a[middle]
        elif a[middle] < target:
            left = middle + 1
            # print("작다")
        elif a[middle] > target:
            right = middle - 1
            # print("크다")
        # print(left,right,middle)
    return None
# arr = list(map(int,input().split()))
# print(BinarySearch(N,arr))
N = int(input())
Narr = list(map(int,input().split()))
M = int(input())
Marr = list(map(int,input().split()))
dic = {}
for i in Narr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] +=1
Narr.sort()
for i in Marr:
    if BinarySearch(i,Narr) != None:
        if i != Marr[-1]:
            print(dic[i],end = " ")
        else:
            print(dic[i])
    else:
        if i != Marr[-1]:
            print(0,end=" ")
        else:
            print(0)


# dic = {}

# 1.자기가 가지고 있는 개수를 센다
# 2.들어오는 거에 맞춰서 있는지 없는지 판단한다.
# 3.있으면 딕셔너리에서 값을 꺼내온다.