N = int(input())
NArr = set(map(int,input().split()))
M = int(input())
MArr = list(map(int,input().split()))
for i in MArr:
    print(1) if i in NArr else print(0)
# set이 중복제거, in 계산할때는 더 빠르다.