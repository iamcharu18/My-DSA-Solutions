#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#


# @lc code=start
# Approach 1: 2 for loops and check whether sum is equal to target and return indices - Time O(n^2) Space O(1)
# Approach 2: copy array and sort that, use two pointers - Time O(nlogn) Space O(n)
# Approach 3: use hashmap and while iterating once through array, check if the difference already exists - O(n), O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevFreq = {}

        for index, val in enumerate(nums):
            diff = target - val
            if diff in prevFreq:
                return [prevFreq[diff], index]
            prevFreq[val] = index

        # Approach 2 Solution
        # sorted_nums = sorted(nums)
        # i, j = 0, len(nums) - 1
        # while i < j:
        #     if sorted_nums[i] + sorted_nums[j] == target:
        #         break
        #     elif sorted_nums[i] + sorted_nums[j] < target:
        #         i += 1
        #     else:
        #         j -= 1
        # index1 = nums.index(sorted_nums[i])
        # index2 = len(nums) - nums[::-1].index(sorted_nums[j]) - 1

        # return [min(index1, index2), max(index1, index2)]


# @lc code=end
