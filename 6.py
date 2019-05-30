n=int(input())
a=list(map(int,input().split()))
l=[]
r=[]
for i in range(n):
    if(a[i]not in l):
        l.append(a[i])
    else:
        r.append(a[i])
if(r !=0):
    print(r[0])
else:
    print("unique")
