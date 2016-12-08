# Given a non-empty integer array of size n,
# find the minimum number of moves required to make all array elements
# equal, where a move is incrementing n - 1 elements by 1.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 3
#
# Explanation:
# Only three moves are needed (remember each move increments two elements):
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

# Solution: [1,2,3] => [1,2,2] => [1,1,2] => [1,1,1]
# So the minimum number of moves is equal Sum(nums) - minimum(nums)*len(nums)
# it's means that 2 - 1 + 3 - 1 = 3


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sum(nums) - min(nums) * len(nums)

if __name__ == '__main__':
    result = Solution().minMoves([1,2,3,4])
    print result
