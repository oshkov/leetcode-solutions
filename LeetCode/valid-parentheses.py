'''
https://leetcode.com/problems/valid-parentheses/description/

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
'''

class Solution(object):
    def isValid(self, s):
        need = []
        for skobochka in s:
            if skobochka == '(':
                need.append(')')
            elif skobochka == '[':
                need.append(']')
            elif skobochka == '{':
                need.append('}')
            elif skobochka in [')',']','}']:
                if len(need) != 0:
                    if skobochka == need[-1]:
                        need.pop()
                    else:
                        return False
                else:
                    return False
        if len(need) == 0:
            return True
        else:
            return False

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        skobochki = {'(': ')', '[': ']', '{': '}'}
        need = []
        for skobochka in s:
            if skobochka in skobochki.keys():
                need.append(skobochki.get(skobochka))
            elif skobochka in skobochki.values():
                if len(need) != 0:
                    if skobochka == need[-1]:
                        need.pop()
                    else:
                        return False
                else:
                    return False
        if len(need) == 0:
            return True
        else:
            return False

print(Solution.isValid(Solution, "[]"))