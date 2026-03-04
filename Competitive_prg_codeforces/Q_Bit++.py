n=int(input())
val=0
for i in range(n):
    str1=input()
    if str1.upper()=='++X' or str1.upper()=='X++':
        val+=1
    else:
        val-=1
print(val)