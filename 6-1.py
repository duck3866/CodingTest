import datetime
import random
import time
b=[]
print("*******오늘의 로또*********")
c = datetime.datetime.now()
print("오늘은 %d년 %d월 %d일" %(c.year, c.month, c.day))
print("3초뒤 알려드립니다.")
for i in range(3,0,-1):
    print(i)
    time.sleep(1)
while len(b)!=7:
    a=random.randrange(1,46)
    if a not in b:
        b.append(a)
print('결과')
for i in b:
    print(i)