a = int(input())
namu = [64]
while True:
    if sum(namu) == a:
        print(len(namu))
        break
    if sum(namu) > a:
        wjfqks = min(namu)//2
        namu.remove(min(namu))
        namu.append(wjfqks)
        if sum(namu) < a:
            namu.append(wjfqks)