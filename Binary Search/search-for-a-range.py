# Time:  O(logn)
# Space: O(1)
#
# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
#

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Find the first index where target <= nums[index]
        left = self.binarySearch(lambda x, y: x >= y, nums, target)

        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        right = self.binarySearch(lambda x, y: x > y, nums, target)
        return [left, right - 1]

    def binarySearch(self, compare, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) / 2
            if compare(nums[mid], target):
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    print Solution().searchRange([2, 2], 3)
    print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
