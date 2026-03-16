class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, alt = set(), set()
        rows, cols = len(heights), len(heights[0])
        res = []

        def dfs(r, c, visited, prevHeight):
            # not qualified
            if r > rows - 1 or c > cols - 1 or \
                r < 0 or c < 0 or heights[r][c] < prevHeight or (r, c) in visited:
                return 

            visited.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
            
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, alt, heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, alt, heights[r][cols - 1])
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in alt:
                    res.append([r, c])
        return res
        