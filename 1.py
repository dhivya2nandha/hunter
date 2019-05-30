n=int(input())
a=list(map(int,input().split()))
l=[]
r=[]
for i in range(n):
    if(a[i]not in l):
        l.append(a[i])
    else:
        if(a[i] not in r):
            r.append(a[i])
r.sort()
print(r)
