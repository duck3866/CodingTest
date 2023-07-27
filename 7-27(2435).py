n,k = map(int,input().split())
ar = list(map(int,input().split()))
b = []
for i in range(0,len(ar),(k+1)-k):
    b.append(ar[i:k+i])
for j in range(len(b)):
    b[j] = sum(b[j])
print(max(b))