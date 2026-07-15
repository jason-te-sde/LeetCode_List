class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        


        m = len(grid)
        n = len(grid[0])

        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4
                    # bottom
                    if 0 <= i + 1 < m and grid[i + 1][j] == 1:
                        perimeter -= 2

                    #right
                    if 0 <= j + 1 < n and grid[i][j + 1] == 1:
                        perimeter -= 2
        return perimeter

       