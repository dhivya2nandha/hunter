n=int(input())
a=[int(i) for i in input().split()]
t=a[::-1]
for i in range(0,n):
    print(t[i],end="->")
