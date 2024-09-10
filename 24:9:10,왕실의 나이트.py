array = [[0 for col in range(8)] for row in range(8)]
word = ['a','b','c','d','e','f','g','h']
for i in range(8):
    for j in range(1,9):
        array[i][j-1] = word[j-1] + str(i+1)
for i in range(8):
    print(array[i])
controll = input()
moveIndex = word.index(controll[0]),int(controll[1])-1 #아래 오른쪽
print(moveIndex,array[moveIndex[0]][moveIndex[1]])
cnt = 0
if moveIndex[0] != 7: # h줄이 아닐때 오른쪽 움직이기 가능
    if moveIndex[1]+1 != 1: # 위로 가능
        if moveIndex[1]+1 != 2:
            if array[moveIndex[0]-2][moveIndex[1]+1] is not None:#위로 2칸 오른쪽 1칸
                cnt+=1
                print("아니")
        if array[moveIndex[0]-1][moveIndex[1]+2] is not None:#위로 1칸 오른쪽 2칸
            cnt+=1
            print("이거")
    if moveIndex[1]+1 != 8: # 아래로 가능
        if moveIndex[1]+1 != 7:
            if array[moveIndex[0]+2][moveIndex[1]+1] is not None:#아래로 2칸 오른쪽 1칸
                cnt+=1
                print("왜")
        if array[moveIndex[0]+1][moveIndex[1]+2] is not None:# 아래 1칸 오른쪽 2칸
            cnt+=1
            print("안됨")
if moveIndex[0] != 0: # a 줄이 아닐때 왼쪽 가능
    if moveIndex[1]+1 != 1: # 위로 가능
        if moveIndex[1]+1 != 2:
            if array[moveIndex[0]-2][moveIndex[1]-1] is not None:#위로 2칸 왼쪽 1칸
                cnt+=1
                print("진짜")
        if array[moveIndex[0]-1][moveIndex[1]-2] is not None:#위로 1칸 왼쪽 2칸
            cnt+=1
            print("모르")
    if moveIndex[1]+1 != 8: # 아래로 가능
        if moveIndex[1]+1 != 7:
            if array[moveIndex[0]+2][moveIndex[1]-1] is not None:#아래로 2칸 왼쪽 1칸
                cnt+=1
                print("겠")
        if array[moveIndex[0]+1][moveIndex[1]-2] is not None:#아래로 1칸 왼쪽 2칸
            cnt+=1
            print("노")
print(cnt)
#수평 두칸 이동후 수직 한 칸 이동
#수직 한 칸 이동 뒤 수평 한칸