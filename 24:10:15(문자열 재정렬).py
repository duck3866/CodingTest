word = ['A','B','C','D','E','F','G','F','I','J','K','L','N','M','O','P','Q','R','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9']
n = input()
new_n = ""
value = 0
for i in range(len(word)):
    if len(new_n) == len(n):
        break
    for j in range(len(n)):
        if word[i] == n[j]:
            if str.isdigit(n[j]):
                value += int(n[j])
            else:
                new_n += n[j]
        
print(new_n+str(value))