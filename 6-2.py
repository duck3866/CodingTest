a=int(input())
b=[]
cnt=0
cnt2=0
e=0
for i in range(1,a+1):
    b.append(input())

for i in range(len(b)):
    
    if int(b[i])>e:
        e=int(b[i])
        cnt+=1
print(cnt)
print('------------------')
for i in range(1,len(b)+1):
    if b[-i]>b[-i]+1:
        b.pop(-i)+1
    print(b[-i])
print(b)
        
        
    