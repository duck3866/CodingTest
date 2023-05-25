import random
print("%d번" %(random.randint(1, 5)))
a = random.sample(range(1,6), 5)
for i in a:
    print(i,'번')


