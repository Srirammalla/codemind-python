n=int(input())
su=0
while n>9:
    while n>0:
        t=n%10
        su+=t
        n=n//10
    n=su
    su=0
print(n)