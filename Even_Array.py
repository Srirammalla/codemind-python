def prm(n):
    for i in n:
        if i%2==1:
            return False
    return True
n=int(input())
ls=list(map(int,input().split()))
print(prm(ls))