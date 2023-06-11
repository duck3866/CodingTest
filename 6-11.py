while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    if b%a==0:
        print('factor')
    elif a%b==0:
        print('multiple')
    else:
        print('neither')
# 8 16
# 32 4
# 17 5
# 0 0