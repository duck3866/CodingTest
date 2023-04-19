
while -1828:
	m=input()
	s=int(input())
	if s==0 or m=='0':
		break
	if m=='/': 
		for i in range(s,0,-1):
			print(' '*(i-1) + '*'*2)#슬래쉬
	else:
		for j in range(0,s):
			print(' '*j +'*'*2 )
print("프로그램 종료")