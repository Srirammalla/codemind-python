n=int(input())
sm=0
while n>9:
    while n:
        t=n%10
        sm=sm+(t*t)
        n=n//10
    n=sm
    sm=0
if n==1 or n==7:
    print("True")
else:
    print("False")