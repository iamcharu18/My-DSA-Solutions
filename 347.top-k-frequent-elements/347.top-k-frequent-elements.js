/*
 * @lc app=leetcode id=347 lang=javascript
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    let freqCounter = new Map();
    for (let num of nums) {
        freqCounter.set(num, 1 + (freqCounter.get(num) ? freqCounter.get(num) : 0))
    }

    let count = new Array(nums.length + 1).fill(null).map(() => []);
    for (const [key, val] of freqCounter) {
        count[val].push(key);
    }

    let ans = [];
    for (let i = nums.length; i > 0; i--) {
        for (let num of count[i]) {
            ans.push(num);
            if (ans.length == k) {
                console.log(ans);
                return ans;
            }
        }
    }
};
// @lc code=end

