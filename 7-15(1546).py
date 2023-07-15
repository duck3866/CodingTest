a = int(input())
b = list(map(int,input().split()))
c = max(b)
nb = []
for i in b:
    nb.append(i/c*100)
print(sum(nb)/len(b))