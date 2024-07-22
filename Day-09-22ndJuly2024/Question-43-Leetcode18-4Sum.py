'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for l in range(len(nums) - 3):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            for i in range(l + 1, len(nums) - 2):
                if i > l + 1 and nums[i] == nums[i - 1]:
                    continue
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    total = nums[l] + nums[i] + nums[j] + nums[k]
                    if total == target:
                        result.append([nums[l], nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                        j += 1
                        k -= 1
                    elif total < target:
                        j += 1
                    else:
                        k -= 1
        return result