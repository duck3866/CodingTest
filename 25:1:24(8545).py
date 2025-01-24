n = input()
newWord = ""
for i in range(len(n),0,-1):
    newWord += n[i-1]
print(newWord)