'''Given a positive integer, check whether it has alternating bits: namely, 
    if two adjacent bits will always have different values.

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101'''

#code


def hasAlternatingBits(n) -> bool:
    s=''
    while n!=1:
        k=n%2
        if len(s)!=0 and s[0]==str(k):
            return False
        s=str(k)+s
        n=n//2
    if n==1:
        if  len(s)!=0 and s[0]=='1':
            return False
        else:
            return True
            
print(hasAlternatingBits(7))

# first i checked the string is not empty and the adjacent value is not same if not i need to add this 
#   to the string this is done till total bit manuplation