# «One dragon. Two dragon. Three dragon», — the princess was counting. She had trouble falling asleep, and she got bored of counting lambs when she was nine.

# However, just counting dragons was boring as well, so she entertained herself at best she could. Tonight she imagined that all dragons were here to steal her, and she was fighting them off. Every k-th dragon got punched in the face with a frying pan. Every l-th dragon got his tail shut into the balcony door. Every m-th dragon got his paws trampled with sharp heels. Finally, she threatened every n-th dragon to call her mom, and he withdrew in panic.

# How many imaginary dragons suffered moral or physical damage tonight, if the princess counted a total of d dragons?

# Input
# Input data contains integer numbers k, l, m, n and d, each number in a separate line (1 ≤ k, l, m, n ≤ 10, 1 ≤ d ≤ 105).

# Output
# Output the number of damaged dragons.


import math
k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
c=0
if k==1:
    print(d)
else:
    # Count numbers divisible by each of k, l, m, n individually.
    # This overcounts numbers divisible by multiple values.
    single_sum=((d//k)+(d//l)+(d//m)+(d//n))
    def lcm_val(a,b):
        return (a*b)//math.gcd(a,b)
    k_l=d//lcm_val(k,l)
    k_m=d//lcm_val(k,m)
    k_n=d//lcm_val(k,n)
    l_m=d//lcm_val(l,m)
    l_n=d//lcm_val(l,n)
    m_n=d//lcm_val(m,n)
    # Subtract counts of numbers divisible by each pair (using LCM),
    # because they were counted twice in the single_sum.
    pair_sum=k_l+k_m+k_n+l_m+l_n+m_n
    # Add back counts of numbers divisible by each triplet,
    # because they were subtracted more than once in the pair step.
    k_l_m=d//lcm_val(lcm_val(k,l),m)
    k_l_n=d//lcm_val(lcm_val(k,l),n)
    k_m_n=d//lcm_val(lcm_val(k,m),n)
    l_m_n=d//lcm_val(lcm_val(l,m),n)
    triplet_sum=k_l_m+k_l_n+k_m_n+l_m_n
    # Subtract numbers divisible by all four values,
    # as they were added again in the previous step.
    k_l_m_n=d//lcm_val(lcm_val(lcm_val(k,l),m),n)
    print((single_sum)-(pair_sum)+(triplet_sum)-(k_l_m_n))
