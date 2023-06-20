#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
# Approach 1: use 2 for loops, go on multiplying except element itself -> O(n^2)
# Not Valid (because of zeroes) Approach 2: get the multiplied value of all elements, divide it with each element -> O(n)
# Approach 3: get prefix and postfix multiples of each element and multiply them at end => O(n), O(n)
# Approach 4: but storing prefix and postfix as integers -> O(n), O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in range(len(nums))]
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            ans[i] = prefix
            prefix = prefix * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix = postfix * nums[i]

        return ans

        # prefix = [1 for _ in range(len(nums))]
        # postfix = [1 for _ in range(len(nums))]

        # for i in range(1, len(nums)):
        #     prefix[i] = prefix[i] * prefix[i - 1] * nums[i - 1]

        # for i in range(len(nums) - 2, -1, -1):
        #     postfix[i] = postfix[i] * postfix[i + 1] * nums[i + 1]

        # for i in range(len(nums)):
        #     ans.append(prefix[i] * postfix[i])

        # return ans


# @lc code=end
