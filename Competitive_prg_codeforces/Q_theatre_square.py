import math
n,m,a=map(int,input().split())
print(math.ceil(n/a)*math.ceil(m/a))
#to cover the rectangle we do n/a and m/a also to cover the edges we do ceil to add an extra falgstone