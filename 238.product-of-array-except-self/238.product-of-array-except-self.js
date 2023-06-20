/*
 * @lc app=leetcode id=238 lang=javascript
 *
 * [238] Product of Array Except Self
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
    let ans = new Array(nums.length);
    let prefix = 1;
    let postfix = 1;

    let i;
    for (i = 0; i < nums.length; i++) {
        ans[i] = prefix;
        prefix *= nums[i];
    }

    for (i = nums.length - 1; i >= 0; i--) {
        ans[i] *= postfix;
        postfix *= nums[i];
    }

    return ans;
};
// @lc code=end

