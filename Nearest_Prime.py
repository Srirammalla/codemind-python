def prm(n):
    for _ in range(2,int(n**0.5)+1):
        if n%_==0:
            return True
    return False
n=int(input())
for _ in range (0,n):
    t=int(input())
    s=t
    while prm(s):
        s+=1
    u=t
    while prm(u):
        u-=1
    if (s-t)>(t-u):
        print(u)
    elif(s-t)==(t-u):
        print(u)
    else:
        print(s)