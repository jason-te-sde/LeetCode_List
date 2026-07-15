class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
            tag : graph, bfs
            tc. : O(mn)
            sc. : O(mn) 
        """

        if not heights: return []
        

        p_queue = deque()
        a_queue = deque() 

        m, n = len(heights), len(heights[0])
        for i in range(m):
            p_queue.append((i, 0))
            a_queue.append((i, n - 1))
        for j in range(n):
            p_queue.append((0, j))
            a_queue.append((m - 1, j))

        def bfs(queue):
            visited = set(queue)
            directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited \
                    and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            return visited
        
        p_visited = bfs(p_queue)
        a_visited = bfs(a_queue)

        return list(p_visited & a_visited)

                


        
        
        


