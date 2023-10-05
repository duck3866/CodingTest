a = input()
flag = 0
for i in range(1,len(a)):
    cnt = 0
    word = []
    notword = []
    word.append(a[:i])
    notword.append(a[i:])
    wordcnt = 1
    nwordcnt = 1
    for j in range(len(word[0])):
        wordcnt *= int(word[0][j])
    for k in range(len(notword[0])):
        nwordcnt *= int(notword[0][k])
    if wordcnt == nwordcnt:
        cnt+= 1
    if cnt >= 1:
        print('YES')
        flag +=1
        break
if flag == 0:
    print("NO")