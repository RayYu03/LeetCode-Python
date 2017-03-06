# Time:  O(logn)
# Space: O(1)
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, len(nums)
        target = nums[-1]

        while left < right:
            mid = left + (right - left) / 2

            if nums[mid] <= target:
                right = mid
            else:
                left = mid + 1
        return nums[left]

if __name__ == "__main__":
      print Solution().findMin([4, 5, 6, 7, 0, 1, 2])
