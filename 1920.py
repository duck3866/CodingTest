def BinarySearch(target, a):
    find = 0
    left = 0
    right = len(a)-1
    middle = len(a) // 2
    # print("타겟:중간값",target,middle)
    while left < right:
        if a[middle] < target:
            left = middle + 1
            # print("작다")
        elif a[middle] > target:
            right = middle - 1
            # print("크다")
        middle = (left + right)//2
        if a[middle] == target:
            find = middle
            return True#find
        # print(left,right,middle)
    return False
# arr = list(map(int,input().split()))
# print(BinarySearch(N,arr))
result = []
N = int(input())
Narr = list(map(int,input().split()))
M = int(input())
Marr = list(map(int,input().split()))
Narr.sort()
for i in Marr:
    print(1 if BinarySearch(i,Narr) else 0)
# dic = {}

# 1. 지가 가지고 있는 카드가 들어온다.
# 2. 몇개인지 묻는 카드가 들어온다.
# 3. 개수를 출력한다.
