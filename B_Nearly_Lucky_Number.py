n=input()
length=len(n)
a=0
b=0
if "4" in n:
    a=n.count("4")
if "7" in n:
    b=n.count("7")
if a+b==7 or a+b==4:
    print("YES")
else:
    print("NO")