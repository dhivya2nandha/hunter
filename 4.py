n=int(input())
a=list(map(int,input().split()))
l=[]
r=[]
for i in range(n):
    if(a[i]not in l):
        l.append(a[i])
    else:
        r.append(a[i])
le=len(l)
for j in range(le):
    if(l[j] not in r):
        print(l[j])
