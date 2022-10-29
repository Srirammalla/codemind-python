n=int(input())
a=0
b=1
fl=False
while a<=n and b<=n:
    a=b+a
    b=b+a
    if n==a or n==b:
       fl=True
       break
if fl or n==0 or n==1:
    print(True)
else:
    print(False)