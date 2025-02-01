# 1. 전부 돌면서 앞자리 가장 큰거 찾음
# 2. 그거 새로운 리스트에 추가하고 제거
# 3. 전부 반복


N = int(input())
arr = list(input().split())
newArr = []
for i in range(N):
    check = "0"
    # print(arr[i][0])
    for j in arr: # 이번 회차 가장 큰 앞자리 수 구하는거
        if int(j[0]) >= int(check[0]):
            # 1.둘다 앞자리가 같다 ex) "3" : "3"0
            if int(j[0]) == int(check[0]):
                if len(j) >= 2:
                    if int(j+check) > int(check+j):
                        check = j
            # 숫자 두 개를 이어붙였을 때 (A+B vs B+A)
            #  더 큰 값을 만드는 쪽이 먼저 오도록 정렬하는 방법을 생각
            else:
                check = (j)
    newArr.append(check) #구한거를 넣고 없앰
    arr.remove(check)
#     print(arr,newArr)
# print(newArr)
# 정답 완성용
word = ""
for k in newArr:
    word += k
print(int(word))