'''
Given an array nums[] of size n, construct a Product Array P (of same size n) such that P[i] is equal to the product of all the elements of nums except nums[i].

 

Example 1:

Input:
n = 5
nums[] = {10, 3, 5, 6, 2}
Output:
180 600 360 300 900
Explanation: 
For i=0, P[i] = 3*5*6*2 = 180.
For i=1, P[i] = 10*5*6*2 = 600.
For i=2, P[i] = 10*3*6*2 = 360.
For i=3, P[i] = 10*3*5*2 = 300.
For i=4, P[i] = 10*3*5*6 = 900.
Example 2:

Input:
n = 2
nums[] = {12,0}
Output:
0 12
'''

class Solution:
    def productExceptSelf(self, nums, n):
        setnums = set(nums)
        prod = float("inf")
        
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                start = i
                prod = nums[i]
                break
        
        if prod == float("inf") or nums.count(0) > 1:
            return [0] * len(nums)
        
        for i in range(start + 1, len(nums)):
            if nums[i] != 0:
                prod *= (nums[i])
                
        res = []
        for i in nums:
            if i == 0:
                res.append(prod)
            else:
                if 0 in setnums:
                    res.append(0)
                else:
                    res.append(prod // i)
        return res