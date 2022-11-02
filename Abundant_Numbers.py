n=int(input())
sm=0
for _ in range(1,n//2+1):
    if n%_==0:
        sm=sm+_
if sm>n:
    print("True")
else:
    print("False")