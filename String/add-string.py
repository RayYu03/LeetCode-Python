# Time:  O(n)
# Space: O(1)

# Given two non-negative numbers num1 and num2 represented as string,
# return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or
# convert the inputs to integer directly.


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        i, j, carry = len(num1) - 1, len(num2) - 1, 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += ord(num1[i]) - ord('0');
                i -= 1
            if j >= 0:
                carry += ord(num2[j]) - ord('0');
                j -= 1
            result.append(str(carry % 10))
            carry /= 10
        result.reverse()

        return "".join(result)

class Solution2(object):
    def addStrings(self,a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res, carry, val = "", 0, 0
        for i in xrange(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = val / 10, val % 10
            res += str(val)
        if carry:
            res += str(carry)
        return res[::-1]

if __name__ == '__main__':
    result1 = Solution().addStrings("101","200")
    result2 = Solution2().addStrings("101","200")
    assert result1 == result2
