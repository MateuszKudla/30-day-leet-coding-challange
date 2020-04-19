from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        for row in grid:
            row.reverse()
        grid.reverse()
        
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
				
        return grid[-1][-1]
        


if __name__ == "__main__":
    solution = Solution()
    result = solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
    print (result)