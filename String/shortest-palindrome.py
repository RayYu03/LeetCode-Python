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

# Time:  O(n)
# Space: O(n)
# Manacher's Algorithm
class Solution2(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def preProcess(s):
            if not s:
                return ['^', '$']
            string = ['^']
            for c in s:
                string +=  ['#', c]
            string += ['#', '$']
            return string

        string = preProcess(s)
        palindrome = [0] * len(string)
        center, right = 0, 0

        for i in xrange(1, len(string) - 1):
            if right > i:
                palindrome[i] = min(right - i, palindrome[2 * center - i])
            else:
                palindrome[i] = 0

            while string[i + 1 + palindrome[i]] == string[i - 1 - palindrome[i]]:
                palindrome[i] += 1

            if i + palindrome[i] > right:
                center, right = i, i + palindrome[i]

        max_len = 0
        for i in xrange(1, len(string) - 1):
            if i - palindrome[i] == 1:
                max_len = palindrome[i]
        print max_len
        return s[len(s)-1:max_len-1:-1] + s

if __name__ == "__main__":
    print Solution2().shortestPalindrome("aacecaaa")
