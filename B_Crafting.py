t=int(input())
for _ in range(t):
    n=int(input())
    a1=list(map(int,input().split()))
    b1=list(map(int,input().split()))
    diff=0
    count=0
    for i in range(n):
        if b1[i]-a1[i]>0:
            if b1[i]-a1[i]>diff:
                diff=b1[i]-a1[i] 
            count+=1
    # print(diff)
    # print(count)
    if count>1:
        print("NO")
    elif count==0:
        print("YES")
    else:  
        for i in range(n):
            if a1[i]>=b1[i]:
                if a1[i]-b1[i]>=diff:
                    continue
                else:
                    print("NO")
                    break
        else:
            print("YES")







