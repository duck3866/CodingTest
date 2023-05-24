import sys

Blacklist = ["김동찬", "이성은", "이슬아"]

def Male(Dad, Mom, Name) :
    if Name in Blacklist :
        return 159.4

    return ((Mom + 13) + Dad) / 2 + 10

def Female(Dad, Mom, Name) :
    if Name in Blacklist:
        return 159.4

    return ((Dad - 13) + Mom) / 2 + 10

print("---------------------------------------------")
print("| 다리가 짧으신 분들을 위한 예상키 계산기 ! |")
print("---------------------------------------------", end='\n\n')

print("이름을 입력해주세요 .\n=> ", end='')
Name = sys.stdin.readline().rstrip()

print("아빠키를 입력해주세요 .\n=> ", end='')
Dad = float(sys.stdin.readline().rstrip())

print("엄마키를 입력해주세요 .\n=> ", end='')
Mom = float(sys.stdin.readline().rstrip())

print("성별을 선택해주세요 . (숫자)\n1) 남자\n2) 여자\n=> ", end='')

while True :
    Gen = int(sys.stdin.readline().rstrip())

    if type(Gen) != int or Gen < 0 or Gen > 2:
        print("다시 입력해주세요.\n=> ", end='')

    else :
        if Gen == 1 :
            print("예상키 : " + str(Male(Dad, Mom, Name)))
            break
        else :
            print("예상키 : " + str(Female(Dad, Mom, Name)))
            break

# 저작권은 엄성민에게 있습니다. ^^