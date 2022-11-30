n,t=map(int,input().split())
if t<n:
    n,t=t,n
if n==t-1 or n==t+1:
    print("Yes")
elif n==1 and t==10:
    print("Yes")
else:
    print("No")