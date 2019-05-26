n=int(input())
count=0
while(n>0):
    t=n%10
    count=count+(t*t)
    n=n//10
print(count)
