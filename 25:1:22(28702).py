command = []
kk = 0
cnt = 0
for i in range(1,4):
    word = (input())
    if not (word.isalpha()):
        cnt = i
        kk = int(word)
check = kk + (4-cnt)
if check % 3 == 0 and check % 5 == 0:
    print("FizzBuzz")
elif check % 3 == 0:
    print("Fizz")
elif check % 5 == 0:
    print("Buzz")
else:
    print(check)
