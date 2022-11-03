def prm(n):
    if n==1:
        return False
    for _ in range (2,int(n**0.5)+1):
        if n%_==0:
            return False
    return True
n=int(input())
s=int(input())
t=0
while n<=s:
    if prm(n):
        t+=1
    n+=1
print(t)