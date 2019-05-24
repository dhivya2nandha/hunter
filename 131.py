n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
while(len(l)!=0):
    m=min(l)
    print(m)
    l.remove(m)
    ma=max(l)
    print(ma)
    l.remove(ma)
