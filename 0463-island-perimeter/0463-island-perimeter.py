class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        perimeter = 0
        directions = [[0, 1], [1, 0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4
                    for x, k in directions:
                        if 0 <= i + x < m and 0 <= j + k < n and grid[i + x][j + k] == 1:
                            perimeter -= 2
        return perimeter
