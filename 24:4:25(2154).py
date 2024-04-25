word = input()
s = 0
for i in word:
    if ord(i) > 91:
        s += ord(i) - 96
    else:
        s += ord(i) - 38
cnt = 0
for j in range(2,s-1):
    if s % j == 0:
        cnt +=s-1
        break
if cnt == 0:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
