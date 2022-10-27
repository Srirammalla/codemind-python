n=int(input())
z=0
o=0
t=0
h=0
f=0
v=0
s=0
e=0
i=0
y=0
while n:
    r=n%10
    if r==0:
        z+=1
    elif r==1:
        o+=1
    elif r==2:
        t+=1
    elif r==3:
        h+=1
    elif r==4:
        f+=1
    elif r==5:
        v+=1
    elif r==6:
        s+=1
    elif r==7:
        e+=1
    elif r==8:
        i+=1
    elif r==9:
        y+=1
    n=n//10
if z>=2 or o>=2 or t>=2 or h>=2 or f>=2 or v>=2 or s>=2 or e>=2 or i>=2 or y>=2:
    print("Not Unique Number")
else:
    print("Unique Number")