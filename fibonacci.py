n=int(input())
a=0
b=1
i=2
print(a,b,end=" ")
while i<=n:
    a=a+b
    b=b+a
    if i<n:
        print(a,end=" ")
    i+=1
    if i<n:
        print(b,end=" ")
    i+=1