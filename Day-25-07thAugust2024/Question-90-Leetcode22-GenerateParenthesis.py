'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(open, close, s):
            if close == open and close + open == n * 2:
                ans.append(s)
                return
            if open < n:
                dfs(open + 1, close, s + '(')
            if close < open:
                dfs(open, close + 1, s + ')')
        dfs(0, 0, "")
        return ans