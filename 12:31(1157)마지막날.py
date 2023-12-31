b = input()
a = {}
c = []
for j in b:
    if ord(j) <= 90:
        c.append(chr(ord(j) + 32))
    else:
        c.append(j)
for i in c:
    if i not in a:
        a[i] = c.count(i)
sort = sorted(a.items(), key=lambda x: x[1], reverse=True)
if len(sort) > 1 and sort[0][1] == sort[1][1]:
    print('?')
else:
    word = sort[0][0]
    print(word.upper())
