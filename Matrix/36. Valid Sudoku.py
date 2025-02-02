################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/valid-sudoku/
################################################################



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nrow = 9
        ncol = 9
        
        row_set = set()
        cols_dict = {i: set() for i in range(ncol)}
        grid_dict = {i: set() for i in range(ncol)}

        for r in range(nrow):
            for c in range(ncol):
                val = board[r][c]
                # If not filled, just pass
                if val == '.': pass
                # If filled,
                else:
                    # Check row constraint
                    if val in row_set:
                        return False
                    else:
                        row_set.add(val)
                        # Check col constraint
                        if val not in cols_dict[c]:
                            cols_dict[c].add(val)
                        else:
                            return False
                        
                        # Check grid constraint
                        # Calculate grid number as:
                        # (row_num // 3)* 3 + (col_num // 3)
                        gridNum = (r // 3)*3 + (c // 3)
                        if val not in grid_dict[gridNum]:
                            grid_dict[gridNum].add(val)
                        else:
                            return False

            row_set = set()
        
        return True