################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/number-of-islands/
################################################################



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        nrows = len(grid)
        ncols = len(grid[0])

        countIslands = 0

        def mark(row, col):
            if row >= nrows or col >= ncols or row < 0 or col < 0 or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            mark(row - 1, col)
            mark(row + 1, col)
            mark(row, col - 1)
            mark(row, col + 1)


        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == "0":
                    continue
                else:
                    countIslands += 1
                    mark(i, j)
        
        return countIslands
        