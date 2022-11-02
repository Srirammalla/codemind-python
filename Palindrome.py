n=int(input())
s=n
rv=0
while n:
    t=n%10
    rv=rv*10+t
    n=n//10
if rv==s:
    print("True")
else:
    print(False)