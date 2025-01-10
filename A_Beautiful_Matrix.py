matrix=[]
for i in range(5):
    row=list(map(int,input().split()))
    matrix.append(row)
for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            a=i
            b=j
            break
print(abs(2-a)+abs(2-b))