abc = int(input())
arr = []
for i in range(abc):
    d,c = input().split()
    arr.append([d,int(c)])
arr.sort(key=lambda x:(x[1]),reverse=True)#키로 이중배열 정렬 기준
print(arr[2][0])#3번째의 이름 출력