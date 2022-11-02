def rev(n):
    k=n
    sm=0
    while n:
        t=n%10
        sm=sm*10+t
        n=n//10
    if k==sm:
        return False
    else:
        return True
n=int(input())
s=n+1
t=n-1
while rev(s):
    s+=1
while rev(t):
    t-=1
if (s-n)>(n-t):
    print(t)
elif (s-n)==(n-t):
    print(t,s)
else:
    print(s)