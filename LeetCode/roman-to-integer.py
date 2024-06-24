'''
https://leetcode.com/problems/roman-to-integer/description/

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        index = 0
        nums_array = []
        while index < len(s):
            if len(s) - index == 1:
                nums_array.append(numbers.get(s[index]))
                index += 1
            elif numbers.get(s[index]) >= numbers.get(s[index + 1]):
                nums_array.append(numbers.get(s[index]))
                index += 1
            else:
                nums_array.append(numbers.get(s[index + 1]) - numbers.get(s[index]))
                index += 2
        return sum(nums_array)


print(Solution.romanToInt(Solution, 'MMCCCXXIV'))