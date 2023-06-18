a,b=map(int,input().split())
cnt=0
for i in range(1,365,1):
	if i%(a+1)==0 and i%(b+1)==0:
		cnt+=1
print('%d 일 입니다.'%cnt)
