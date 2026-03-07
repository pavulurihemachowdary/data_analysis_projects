matrix=[list(map(int,input().split())) for i in range(5)]
for i in range(5):
    for j in range(5):
        if matrix[i][j]!=0:
            m,n=i,j
print(abs(2-m)+abs(2-n))