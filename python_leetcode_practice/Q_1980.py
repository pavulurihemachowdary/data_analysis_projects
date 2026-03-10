# Description

# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

# Example 1:

# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
# Example 2:

# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
# Example 3:

# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 
#i solved by the brute force approach, where i first converted the binary list to integers and then populated the 
# integers that are not in that list and converted back to binary by appending 0's if they are not exactly of the length of other binary strings
# also without iterating throught out the list i just returned the first appended item from the list.
def findDifferentBinaryString(nums):
        lt=list(int(i,2) for i in nums)
        lt1=[]
        for i in range(2*len(nums)):
            if i not in lt:
                a=bin(i)[2:]
                if len(a)<len(nums):
                    lt1.append("0"*(len(nums)-len(a))+a)
                    continue
                lt1.append(a)
                break
        return lt1[0]

#without doing all this we can just do the take one item from each of the nums[i] and replace any of the nus[i][i] with its opposite 
# this is very intelligent way of solving and i found it worth to be noted
def findDifferentBinaryString2(nums):
     lt=[]
     for i in range(len(nums)):
        if nums[i][i]=="0":
            lt.append("1")
        elif nums[i][i]=="1":
            lt.append("0")
     return "".join(lt)

print(type(findDifferentBinaryString2(["11","00"])))