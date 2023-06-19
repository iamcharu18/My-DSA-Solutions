/*
 * @lc app=leetcode id=49 lang=javascript
 *
 * [49] Group Anagrams
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
    let res = new Map();

    for (const s of strs) {
        let count = new Array(26).fill(0);
        for (const ch of s) {
            count[ch.charCodeAt(0) - 'a'.charCodeAt(0)]++;
        }
        count = count.toString();
        const values = res.get(count) || [];
        values.push(s);
        res.set(count, values);
    }

    return [...res.values()];
};
// @lc code=end

