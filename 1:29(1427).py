a = input()
b = []
for i in a:
    b.append(int(i))
b.sort(reverse = True)
d = map(str,b)
dd = ''.join(d)
print(dd)
