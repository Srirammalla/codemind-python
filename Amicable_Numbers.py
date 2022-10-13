def val(a):
    i=1
    am=0
    while i<a:
        if a%i==0:
         am+=i
        i+=1
    return am
s=int(input())
t=int(input())
if s==val(t) and t==val(s):
    print("Amicable")
else :
    print("Not Amicable")