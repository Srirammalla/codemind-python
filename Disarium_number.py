def rev(n):
    sm=0
    while n:
        t=n%10
        sm=sm*10+t
        n=n//10
    return sm
n=int(input())
t=rev(n)
i=1
u=0
while t:
    s=t%10
    u=u+(s**i)
    t=t//10
    i+=1
if u==n:
    print("True")
else:
    print("False")