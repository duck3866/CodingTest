while True:
    a = input()
    na =''
    if a == '0':
        break
    for i in a:
        na = i+na
    if a == na:
        print('yes')
    else:
        print('no')
        