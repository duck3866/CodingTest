a = int(input())
for i in range(a):
    Dic = {"TTT":0,"TTH":0,"THT":0,"THH":0,"HTT":0,"HTH":0,"HHT":0,"HHH":0}
    b = input()
    for i in range(len(b)-2):
        ehdwjs = []
        ehdwjs.append(b[i])
        ehdwjs.append(b[i+1])
        ehdwjs.append(b[i+2])
        coin = ''.join(ehdwjs)
        Dic[coin] += 1
    print(' '.join(map(str, Dic.values())))
