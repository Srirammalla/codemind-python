n=int(input())
t=1
for _ in range (2,int(n**0.5)+1):
    if n%_==0:
        print("not a prime")
        t=0
        break
if t:
    print("prime")