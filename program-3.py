n=int(input())
i=1
if n%2==0:
    n=n-1
    while i<=n*2:
        print(i,end=",")
        i=i+2
else:
    while i<=n*2:
        print(i,end=",")
        i=i+2

     
