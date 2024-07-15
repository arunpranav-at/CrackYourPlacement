'''
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
'''

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1} # to store remainders
        prefixSum = 0
        result = 0
        for i in nums:
            prefixSum += i
            remainder = prefixSum % k
            if remainder < 0:
                remainder += k
            if remainder in hashmap:
                result += hashmap[remainder]
                hashmap[remainder] += 1
            else:
                hashmap[remainder] = 1
        return result