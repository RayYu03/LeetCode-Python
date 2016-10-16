# Time:  O(n)
# Space: O(1)
#
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a subarray of which the sum  s. If there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
#

# Sliding window solution.
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        start = 0
        sum = 0
        min_size = float("inf")
        for i in xrange(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_size = min(min_size, i - start + 1)
                sum -= nums[start]
                start += 1

        return min_size if min_size != float('inf') else 0

if __name__ == '__main__':
    result = Solution().minSubArrayLen(7,[2,3,1,2,4,3])
    print result
