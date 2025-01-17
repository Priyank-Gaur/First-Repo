n,m=map(int,input().split())
x,y=map(int,input().split())
x1=list(map(int,input().split()))
y1=list(map(int,input().split()))
lst=[]
lst1=[]
lst2=[]
if len(x1)==1:
    z=x1[0]-0
    c=n-x1[0]
    lst.append(z)
    lst.append(c)
    
else:
    for i in range(len(x1)-1):
        m=x1[i+1]-x1[i]
        lst.append(m)
if len(y1)==1:
    d=y1[0]-0
    e=m-y1[0]
    lst1.append(d)
    lst1.append(e)
    
else:
    for i in range(len(y1)-1):
        p=y1[i+1]-y1[i]
        lst1.append(p)
print(max(lst1)*max(lst))

