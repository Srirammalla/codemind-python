a,b=map(int,input().split())
if a>b:
    a,b=b,a
i=a
while i:
    if a%i==0 and b%i==0:
        print(i)
        break
    i-=1