def prm(n):    
    for _ in range (2,int(n**0.5)+1):
        if n%_==0:
            return False
    return True
n=int(input())
t=int(input())
s=1
while True:
    if prm(n+t+s):
        print(s)
        break
    s+=1