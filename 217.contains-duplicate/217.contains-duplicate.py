#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
# Return false if there are no duplicates in array, else true
# Approach 1: Check for each element whether it is present in the subarray -> Time - O(n^2), Space - O(1)
# Approach 2: Sort and check next element - Time O(nlogn), Space O(1)
# Approach 2: Using Hashmap - O(n) time & Space (or we can use simply set)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freqCounter = {}
        for num in nums:
            if num in freqCounter:
                return True
            freqCounter[num] = 1
        return False

# @lc code=end
