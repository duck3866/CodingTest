# 0칸 :1(1개)
# 1칸 :2 ~ 7까지(6개)
# 2칸 :8 ~ 19까지(12개)
# 3칸 :20 ~ 37까지(18개)
# 4칸 :38 ~ 61까지 (23개)
# 5칸 :62 ~
# 60에서 에러
n = int(input())
x = 6
cnt = 2
line = 1
for i in range(1,n+1):
    if i >= cnt:
        line += 1
        cnt += x
        x += 6
        # print("??",cnt,x)
print(line)