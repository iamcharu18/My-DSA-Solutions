#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
# Approach 1: while iterating, sort that value and check if that already exists or not and add accordingly - O(m*nlogn), O(m)
# Approach 2: just like above, but instead of sorting, use counter to reduce time complexity - O(m*n), O(m)
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            res[tuple(count)].append(s)

        return res.values()


# @lc code=end
