from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < n and 0 <= j < m:
                if grid[i][j] == "1":
                    grid[i][j]  = "-"
                    dfs(i + 1, j)
                    dfs(i, j + 1)
                    dfs(i - 1, j)
                    dfs(i, j - 1)
        
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count

if __name__ == "__main__":
    solution = Solution()
    result = solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
    print (result)