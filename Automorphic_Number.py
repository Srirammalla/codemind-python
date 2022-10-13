s=int(input())
t=s
n=s*s
dig=0
while s>0:
    dig+=1
    s=s//10
r=n%(10**dig)
if r==t:
    print ("Automorphic Number")
else :
    print("Not an Automorphic Number")