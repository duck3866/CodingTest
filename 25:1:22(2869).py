import math
#하루에 올라가는거 A-B 마지막날 A를 더해서 V 도달하면 날짜가 완성됨
A, B, V = map(int,input().split())

goodDay = V - A
day = goodDay/(A-B)
day = math.ceil(day) # 0.25 일은 없다 -> 1일로 올림
print(day + 1) # 먼저 빼둔 1일 추가
# A-B를 한다는 것 마지막 날은 B를 안 뺀다는 것은 알았는데 그 둘을 매칭을 못함
# 이걸 매칭해서 마지막을 미리 빼둬야 하는데...
# day = 0
# mt = 0
# while True:
#     day += 1
#     print("오늘 몇일?",day)
#     mt += A
#     if mt >= V:
#         break
#     print("낮",mt)
#     mt -= B
#     print("밤",mt)
# print(day)