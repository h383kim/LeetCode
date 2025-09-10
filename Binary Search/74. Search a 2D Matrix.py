################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/search-a-2d-matrix/
################################################################



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1

        while t <= b:
            l, r = 0, len(matrix[0]) - 1
            m_row = t + ((b - t) // 2)

            if matrix[m_row][-1] < target:
                t = m_row + 1
            else:
                if matrix[m_row][0] > target:
                    b = m_row - 1
                else:
                    # Binary Search in that row
                    while l <= r:
                        m = l + ((r - l) // 2)
                        if matrix[m_row][m] == target:
                            return True
                        elif matrix[m_row][m] < target:
                            l = m + 1
                        else:
                            r = m - 1

                    return False

        return False