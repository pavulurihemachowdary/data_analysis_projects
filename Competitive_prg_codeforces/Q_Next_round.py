n,k=map(int, input().split())
lt=list(map(int,input().split()))
k_val=lt[k-1]
c=0
for i in lt:
    if i>=k_val and i!=0:
        c+=1
print(c)