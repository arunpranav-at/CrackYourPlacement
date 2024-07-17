'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        if len(strs) > 1:
            for i in range(1, len(strs)):
                curr = strs[i]
                for k in range(max(len(curr), len(ans))):
                    if k >= min((len(curr), len(ans))):
                        ans = curr[:k]
                        break
                    elif curr[k] != ans[k]:
                        ans = curr[:k]
                        break
        return ans