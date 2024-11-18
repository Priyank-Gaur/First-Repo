t=int(input())
for i in range(t):
    n,B,x,y=map(int,input().split())
    seq=[0]
    for i in range(n):
        if seq[i]+x>B:
            if seq[i]-y<=B:
                seq.append(seq[i]-y)
            else:
                break
        elif seq[i]-y>B:
            if seq[i]+x<=B:
                seq.append(seq[i]+x)
            else:
                break
        if seq[i]+x<=B and seq[i]-y<=B:
            seq.append(max(seq[i]+x,seq[i]-y))
    print(sum(seq))
