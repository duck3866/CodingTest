import heapq
n = int(input())
heap = [0] * 10001 #0으로 되어있는 배열(개수 세야 하니까) 10000개 0 ~ 10000
for _ in range(n):
    num = int(input())
    heap[num] += 1
cnt = 0
for i in heap:
    if i != 0:
        for j in range(i):
            print(cnt)
    cnt += 1
# 계수 정렬 https://kill-xxx.tistory.com/entry/python-계수정렬
# for _ in range(n):
#     num = int(input())
#     heapq.heappush(heap, num)
# while heap:
#     print(heapq.heappop(heap))