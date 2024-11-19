t=int(input())
for i in range(t):
    n=int(input())
    a=n
    count=0
    if n<10:
        count=n
        n=a
    elif n<100:
        n=n//10
        count+=n+9
        n=a
    elif n<1000:
        n//=100
        count+=n+18
    elif n<10000:
        n//=1000
        count+=n+27
        n=a
    elif n<100000:
        n//=10000
        count+=n+36
        n=a
    elif n<1000000:
        n//=100000
        count+=n+45
    print(count)


