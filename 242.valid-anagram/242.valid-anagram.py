#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
# Approach 1: Sort both strings and check whether they are equal or not - time O(nlogn) space O(1) - Optimized space solution
# Approach 1: Make frequency counters for both of strings and check whether they are equal or not - Time O(n), Space O(n) n = s+t
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Optimized for space complexity. O(nlogn),O(1)
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False

        freqS, freqT = {}, {}
        for i in range(len(s)):
            freqS[s[i]] = 1 + freqS.get(s[i], 0)
            freqT[t[i]] = 1 + freqT.get(t[i], 0)
        # return freqS == freqT (same as below)
        for c in freqS:
            if freqS[c] != freqT.get(c, 0):
                return False
        return True

# @lc code=end
