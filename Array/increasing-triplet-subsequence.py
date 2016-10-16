# Time:  O(n)
# Space: O(1)

# Given an unsorted array return whether an increasing
# subsequence of length 3 exists or not in the array.

# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k]
# given 0 <= i < j < k <= n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Examples:
# Given [1, 2, 3, 4, 5],
# return true.

# Given [5, 4, 3, 2, 1],
# return false.

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        min_num, a, b = float("inf"), float("inf"), float("inf")
        for c in nums:
            if min_num >= c:
                min_num = c
            elif b >= c:
                a, b = min_num, c
            else:
                return True
            print min_num, a, b
        return False

if __name__ == '__main__':
    result = Solution().increasingTriplet([1, 2, 3, 4, 5])
    print result
