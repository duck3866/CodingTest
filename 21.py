n=int(input())
cnt=0
if n>=10:
	for i in range(1,n+1):
		if i%3==0:
			cnt+=1
	
	print("1~%d 사이의 3의 배수인 숫자는 %d개"%(n,cnt))
	
	
else:
	print("메롱")