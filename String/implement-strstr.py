# Time:  O(n + k)
# Space: O(k)
#
# Implement strStr().
#
# Returns a pointer to the first occurrence of needle in haystack,
#  or null if needle is not part of haystack.
#

# Wiki of KMP algorithm:
# http://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm




# Time:  O(n * k)
# Space: O(k)
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in xrange(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

if __name__ == "__main__":
    print Solution().strStr("a", "")
    print Solution().strStr("abcdef", "cde")
    print Solution().strStr("abababcdab", "ababcdx")
