n=int(input())
lt_main=[]
for i in range(n):
    lt=list(map(int,input().split()))
    lt_main.append(lt)
c=0
for i in lt_main:
    if i.count(1)>=2:
        c+=1
print(c)

  