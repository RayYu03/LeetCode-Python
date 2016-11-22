# Time:  O(n)
# Space: O(1)

# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character
# while preserving the order of characters. No two characters may map to
# the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.

from itertools import izip
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s2t, t2s = dict(), dict()
        for p, w in izip(s, t):
            if w not in s2t and p not in t2s:
                s2t[w] = p
                t2s[p] = w
            elif w not in s2t or s2t[w] != p:
                return False
        return True


# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        lookup = dict()
        for i in xrange(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
        return True


if __name__ == "__main__":
    print Solution().isIsomorphic('egg', 'add')
    print Solution2().isIsomorphic('eegg', 'aadd')
