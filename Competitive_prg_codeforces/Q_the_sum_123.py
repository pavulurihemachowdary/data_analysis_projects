n=int(input())
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    lt=[]
    n1,n2=1,1
    lt.append(n1)
    lt.append(n2)
    for i in range(n-2):
        lt.append(lt[-1]+lt[-2])
    print(sum(lt))
