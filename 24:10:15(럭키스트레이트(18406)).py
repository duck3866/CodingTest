n = input()
middle = int(len(n)/2)
forward = str(n[0:middle])
back = str(n[middle ::])
value1 = 0
value2 = 0
for i in forward:
    value1 += int(i)
for i in back:
    value2 += int(i)
if value1 == value2:
    print("LUCKY")
else:
    print("READY")