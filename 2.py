a=int(input())
b=0
for i in range(a,0,-2):
	print(' '*b,end='')
	for j in range(1,i+1):
		
		print('*',end='')
	b+=1
	print()
