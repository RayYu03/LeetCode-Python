# Time:  O(n)
# Space: O(1)
#
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
#
# For example, the numbers "69", "88", and "818" are all strobogrammatic.

class Solution:
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    def isStrobogrammatic(self, num):
        """
        :type num: string
        :rtype: bool
        """
        n = len(num)
        for i in xrange((n + 1) / 2):
            if num[n - 1 - i] not in self.lookup or \
               num[i] != self.lookup[num[n - 1 - i]]:
                return False
            i += 1
        return True

if __name__ == "__main__":
    print Solution().isStrobogrammatic("8")
