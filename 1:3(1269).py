a,b = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
My_A = set(A)
My_B = set(B)
if a>b:
    c = My_B ^ My_A
else:
    c = My_A ^ My_B
print(len(c))