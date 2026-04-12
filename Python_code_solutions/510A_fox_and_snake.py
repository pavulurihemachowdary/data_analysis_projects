n,m=map(int,input().split())
fl=1
for i in range(n):
    for j in range(m):
        if i%2==0:
            print("#",end="")
        elif i%2!=0 and fl==1:
            if j==m-1:
                print("#", end="")
            else:
                print(".", end="")
        elif i%2!=0 and fl==0:
            if j==0:
                print("#", end="")
            else:
                print(".",end="")
    if i%2!=0:
        if fl==1:
            fl=0
        else:
            fl=1
    print()
