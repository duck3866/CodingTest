n = int(input())
cnt = 0
num = 0
while True:
    num += 1
    if cnt == n:
        break
    if "666" in str(num):
        cnt +=1
    # else:
    #     num +=1
    #     print(num)
print(num - 1)