bf = []
while True:
    str = input()
    if str == ".":
        break
    flag = 0
    b = []
    for i in str:
        if i =="(" or i == "[":
            b.append(i)
        elif len(b) > 0 and (i == ")" or i == "]") :
            if i == ")" and b[-1] == "(":
                b.pop()
            elif i == "]" and b[-1] == "[":
                b.pop()
            else:
                b.append("aaaa")
        elif (i == ")" or i == "]"):
            b.append("aaaa")
    if len(b) == 0:
        bf.append("yes")
    else:
        bf.append("no")
for s in bf:
    print(s)
