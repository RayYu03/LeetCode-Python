# Time:  O(n)
# Space: O(n)
#
# Given a string S, you are allowed to convert it to a palindrome
# by adding characters in front of it. Find and return the shortest
# palindrome you can find by performing this transformation.
#
# For example:
#
# Given "aacecaaa", return "aaacecaaa".
#
# Given "abcd", return "dcbabcd".
#

# KMP Algorithm
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def getPrefix(pattern):
            prefix = [0] * len(pattern)
            j = 0
            for i in xrange(1, len(pattern)):
                while j > 0 and pattern[j] != pattern[i]:
                    j = prefix[j - 1]
                if pattern[j] == pattern[i]:
                    j += 1
                prefix[i] = j
            print prefix
            return prefix

        if not s:
            return s

        A = s + s[::-1]
        prefix = getPrefix(A)
        i = prefix[-1]
        while i >= len(s) + 1:
            i = prefix[i - 1]
        return s[i:][::-1] + s

if __name__ == "__main__":
    print Solution().shortestPalindrome("c")
