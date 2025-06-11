input = input()
word = input.split('-')
# print(word)
value = 0
first = word[0]
two = first.split('+')
for i in two:
    value += int(i)
for j in range(1,len(word)):
    number = word[j].split('+')
    test = 0
    for i in number:
        test += int(i)
    # number = int(number)
    value -= int(test)
print(value)



    