/*
 * @lc app=leetcode id=217 lang=javascript
 *
 * [217] Contains Duplicate
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
    let freqCounter = {};
    for (const num of nums) {
        if (freqCounter[num] === 1) return true;
        freqCounter[num] = 1;
    }
    return false;
};
// @lc code=end

