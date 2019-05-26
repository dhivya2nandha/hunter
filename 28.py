s=input()
l=list(s)
n=len(l)
res=[]
for i in range(n):
    if l[i] not in res:
        res.append(l[i])
t=''.join(res)
print(t)
