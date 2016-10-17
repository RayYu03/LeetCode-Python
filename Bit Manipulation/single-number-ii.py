# Time:  O(n)
# Space: O(1)
#
# Given an array of integers, every element appears three times except for one.
# Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one, two, three = 0, 0, 0
        for x in A:
            three = two & x
            print bin(three)
            two |= one & x
            print bin(two)
            one |= x
            print bin(one)


            two &= ~three
            print bin(two)
            one &= ~three
            print bin(one)

            print
        return one

if __name__ == "__main__":
    print Solution().singleNumber([3,3,1,1])
