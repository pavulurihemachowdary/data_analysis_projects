# Description

# You are given two positive integers 𝑎
#  and 𝑏
# . In one move you can increase 𝑎
#  by 1
#  (replace 𝑎
#  with 𝑎+1
# ). Your task is to find the minimum number of moves you need to do in order to make 𝑎
#  divisible by 𝑏
# . It is possible, that you have to make 0
#  moves, as 𝑎
#  is already divisible by 𝑏
# . You have to answer 𝑡
#  independent test cases.

# Input
# The first line of the input contains one integer 𝑡
#  (1≤𝑡≤104
# ) — the number of test cases. Then 𝑡
#  test cases follow.

# The only line of the test case contains two integers 𝑎
#  and 𝑏
#  (1≤𝑎,𝑏≤109
# ).

# Output
# For each test case print the answer — the minimum number of moves you need to do in order to make 𝑎
#  divisible by 𝑏
# .

# Example
# Input
# 5
# 10 4
# 13 9
# 100 13
# 123 456
# 92 46
# Output
# 2
# 5
# 4
# 333
# 0


t=int(input())
lt=[]
for _ in range(t):
    i,j=map(int,input().split())
    if i%j!=0:
        a=(i-(i%j))+j
        lt.append(a-i)
    else:
        lt.append(0)
for i in lt:
    print(i)