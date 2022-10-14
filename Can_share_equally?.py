s,t=map(int,input().split())
if (s+t)>0:
    if s%2==0 and (t%2==0 or s>0):
        print("YES")
    else:
        print("NO")