/*
 * @lc app=leetcode id=128 lang=javascript
 *
 * [128] Longest Consecutive Sequence
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
    let maxScore = 0;
    const numSet = new Set(nums);

    for (const num of [...numSet]) {
        const prevNum = num - 1;

        if (numSet.has(prevNum)) continue;

        let [currNum, score] = [num, 1];

        const isStreak = () => numSet.has(currNum + 1)
        while (isStreak()) {
            currNum++;
            score++;
        }

        maxScore = Math.max(maxScore, score);
    }

    return maxScore;
};
// @lc code=end

