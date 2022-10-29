n=int(input())
a=0
b=1
fg=True
while a<=n and b<=n:
    a=b+a
    b=b+a
    if a==n or b==n:
        print(True)
        fg=False
        break
if fg:
    print(False)