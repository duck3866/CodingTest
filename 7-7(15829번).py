a = int(input())
word = input()
s = 0   
c = 0       
for i in word:
    s += (ord(i)-96)*(31**c)
    c += 1
    
print(s%234567891)