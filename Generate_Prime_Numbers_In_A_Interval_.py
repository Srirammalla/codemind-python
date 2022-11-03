def prm(n):
    for _ in range (2,int(n**0.5)+1):
        if n%_==0:
            return False
    return True
n=int(input())
t=int(input())
for _ in range(n+1,t+1):
    if prm(_):
        print(_)
    