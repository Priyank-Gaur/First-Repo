t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    count=0
    x=1
    while a<=b:
        a+=x
        x+=1
        count+=1
    print(count)


