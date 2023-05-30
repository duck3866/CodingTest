import random
import time
print("**주사위 프로그램**")
print("3초뒤 알려줍니다")
for i in range(3,0,-1):
    print(i)
    time.sleep(1)
print(random.randrange(1,7))