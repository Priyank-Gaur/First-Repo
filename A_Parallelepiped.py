a,b,c=map(int,input().split())
x=(a*b//c)**0.5
y=(b*c//a)**0.5
z=(a*c//b)**0.5
print(int(4*(x+y+z)))