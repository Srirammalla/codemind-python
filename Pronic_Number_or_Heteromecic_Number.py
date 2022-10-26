n=int(input())
tk=True
for i in range(1,n//2+1):
    if i*(i+1)==n:
        print("YES")
        tk=False
        break
    i+=1
if tk:
    print("NO")
    