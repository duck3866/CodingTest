h,w=map(int,input().split())
if h>150:
    k=h-100
elif h<160:
    k=(h-150)/2+50
else:
    k=(h-100)*0.9
bmi=(h-k)*100/h-k
if bmi <=10:
    print("정상")
elif bmi <=20:
    print("과체중")
else:
    print("비만")