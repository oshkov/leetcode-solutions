'''
https://leetcode.com/problems/longest-common-prefix/description/

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        output_list = list(strs[0])
        for str in strs:
            index = 0

            if len(output_list) > len(str):
                output_list = output_list[:len(str)]
            elif len(output_list) < len(str):
                str = str[:len(output_list)]

            while index < len(output_list):
                if str[index] == output_list[index]:
                    pass
                elif str[index] != output_list[index]:
                    output_list = output_list[:index]
                index += 1

        output = ''.join(output_list)
        return output

print(Solution.longestCommonPrefix(Solution, ["flower","flow","flight"]))