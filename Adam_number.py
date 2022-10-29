def rev(n):
    rv=0
    while n:
        t=n%10
        rv=rv*10+t
        n=n//10
    return rv
n=int(input())
t=n*n
s=rev(n)
if rev(s*s)==t:
    print(True)
else:
    print(False)