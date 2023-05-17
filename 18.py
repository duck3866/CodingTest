a=input()# (입력받은 문자의 ASCII 코드값 * 7) % 80 + 48
for i in a:
    print(chr(ord(i)+2),end='')
print()
for j in a:
    print(chr((ord(j)*7)%80+48),end='')
    