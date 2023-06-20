#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


# @lc code=start
# Approach 1: Frequency counter and return top most by sorting O(nlogn) O(n)
# Approach 2: Same as above but use an array to store keys -> index is frequency, values at index is list of elements -> O(n) O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounter = {}
        for num in nums:
            freqCounter[num] = freqCounter.get(num, 0) + 1

        # return sorted(freqCounter, key=lambda x: freqCounter[x], reverse=True)[:k]

        count = [[] for _ in range(len(nums) + 1)]

        for key, val in freqCounter.items():
            count[val].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res


# @lc code=end
