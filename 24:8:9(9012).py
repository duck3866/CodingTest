n = int(input())
for i in range(n):
    a = input()
    b = []
    for j in a:
        if j == "(":
            b.append(j)
        elif j == ")":
            if len(b)> 0 and b[-1] == "(":
                b.pop()
            else:
                b.append('aaaa')
    if len(b) == 0:
        print("YES")
    else:
        print("NO")
