'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
'''

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n1 = nums[-1]
        n2 = nums[-2]
        n3 = nums[-3]
        n4 = nums[0]
        n5 = nums[1]
        return max(n1*n2*n3, n1*n4*n5)