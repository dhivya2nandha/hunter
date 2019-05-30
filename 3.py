n=int(input())
a=list(map(int,input().split()))
l=[int(i) for i in range(0,n)]
for i in range(n):
    if(a[i]==l[i]):
        print(a[i],end=" ")
else:
    print(-1)
