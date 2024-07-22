'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        answer = 0
        sumDict = dict()
        sumDict[0] = 1
        sizeOfNums = len(nums)
        for i in range(sizeOfNums):
            currSum += nums[i]
            if currSum - k in sumDict:
                answer += sumDict[currSum - k]
            sumDict[currSum] = sumDict.get(currSum, 0) + 1
        return answer