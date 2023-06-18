/*
 * @lc app=leetcode id=242 lang=javascript
 *
 * [242] Valid Anagram
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    if (s.length !== t.length) return false;

    let freqS = new Map();
    let freqT = new Map();

    for (let i = 0; i < s.length; i++) {
        freqS.set(s[i], 1 + (freqS.get(s[i]) ? freqS.get(s[i]) : 0));
        freqT.set(t[i], 1 + (freqT.get(t[i]) ? freqT.get(t[i]) : 0));
    }

    for (let [key, value] of freqS) {
        if (value !== freqT.get(key)) return false;
    }

    return true;
};
// @lc code=end

