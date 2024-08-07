'''
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
'''
from collections import deque
class Solution:
    def numberToWords(self, num: int) -> str:
        def helper2(num):
            teensdic = {
                '0': '',
                '1': 'One',
                '2': 'Two',
                '3': 'Three',
                '4': 'Four',
                '5': 'Five',
                '6': 'Six',
                '7': 'Seven',
                '8': 'Eight',
                '9': 'Nine',
                '00': '',
                '01': 'One',
                '02': 'Two',
                '03': 'Three',
                '04': 'Four',
                '05': 'Five',
                '06': 'Six',
                '07': 'Seven',
                '08': 'Eight',
                '09': 'Nine',
                '10': 'Ten',
                '11': 'Eleven',
                '12': 'Twelve',
                '13': 'Thirteen',
                '14': 'Fourteen',
                '15': 'Fifteen',
                '16': 'Sixteen',
                '17': 'Seventeen',
                '18': 'Eighteen',
                '19': 'Nineteen'
            }
            tensdic = {
                '2': 'Twenty',
                '3': 'Thirty',
                '4': 'Forty',
                '5': 'Fifty',
                '6': 'Sixty',
                '7': 'Seventy',
                '8': 'Eighty',
                '9': 'Ninety'
            }
            if int(num) < 20:
                return "" if teensdic[num] == '' else " " + teensdic[num]
            else:
                t = num[0]
                o = num[1]
                return " " + tensdic[t] + ("" if o == '0' else " " + teensdic[o])

        def helper(num):
            dic = {
                '1': 'One',
                '2': 'Two',
                '3': 'Three',
                '4': 'Four',
                '5': 'Five',
                '6': 'Six',
                '7': 'Seven',
                '8': 'Eight',
                '9': 'Nine'
            } 
            ans = ""
            if len(num) == 3 and num[0] != '0':
                ans += " " + dic[num[0]] + " Hundred"
            if len(num) >= 2:
                ans += helper2(num[-2:])
            elif len(num) == 1:
                ans += " " + dic[num[-1]]
            return ans

        if num == 0:
            return "Zero"
        
        num = str(num)
        n = len(num)
        bunch = deque()
        
        for i in range(n, 0, -3):
            start = max(0, i - 3)
            bunch.appendleft(num[start:i])
        
        bigdic = {
            0: "",
            1: " Thousand",
            2: " Million",
            3: " Billion"
        }
        
        ans = ""
        for i, chunk in enumerate(bunch):
            if int(chunk) != 0:
                ans += helper(chunk) + bigdic[len(bunch) - i - 1]
        
        return ans.strip()