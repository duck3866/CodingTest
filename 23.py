def holsu(*hh) :
	cnt=0
	for i in hh:
		if i%2!=0:
			cnt+=i
	return cnt
	

def bunsic(**zz) :
	return print(zz)
	
print(holsu(1, 2, 4))
print(holsu(7, 12, 5, 20, 64))
bunsic(coffee=3000,milk=1500,tea=4500,latte=5000)