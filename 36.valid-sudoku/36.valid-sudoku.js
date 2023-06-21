/*
 * @lc app=leetcode id=36 lang=javascript
 *
 * [36] Valid Sudoku
 */

// @lc code=start
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
    let rows = new Map();
    let cols = new Map();
    let squares = new Map();

    for (let r = 0; r < board.length; r++) {
        for (let c = 0; c < board[0].length; c++) {
            const val = board[r][c];
            const index = Math.floor(r / 3) * 3 + Math.floor(c / 3);
            if (val === ".") continue;
            if (
                (rows.has(r) && rows.get(r).has(val)) ||
                (cols.has(c) && cols.get(c).has(val)) ||
                (squares.has(index) && squares.get(index).has(val))
            ) {
                return false;
            }
            if (!rows.has(r)) rows.set(r, new Set());
            if (!cols.has(c)) cols.set(c, new Set());
            if (!squares.has(index)) squares.set(index, new Set());
            rows.get(r).add(val);
            cols.get(c).add(val);
            squares.get(index).add(val);
        }
    }

    return true;
};


// @lc code=end

