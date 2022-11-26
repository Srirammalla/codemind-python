def prm (n,t):
    for i in range (t):
        if n[i]%2==1 and i%2==0:
            return False
    return True
n=int(input())
lst=list(map(int,input().split()))
if prm(lst,n):
    print(True)
else:
    print(False)