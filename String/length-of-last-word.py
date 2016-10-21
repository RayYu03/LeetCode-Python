# Time:  O(n)
# Space: O(1)
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.
#

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s:str
        :rtype: int
        """
        length = 0
        for i in reversed(s):
            if i == ' ':
                if length:
                    break
            else:
                length += 1
        return length

# Time:  O(n)
# Space: O(n)
class Solution2:
    def lengthOfLastWord(self, s):
        """
        :type s:str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])
