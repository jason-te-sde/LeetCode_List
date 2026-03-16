class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    island = self.dfs(grid, row, col)
                    res = max(res, island)
        return res
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or \
            col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        
        grid[row][col] = 0

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        area = 1

        for dr, dc in directions:
            area += self.dfs(grid, row + dr, col + dc)
        return area
        
        