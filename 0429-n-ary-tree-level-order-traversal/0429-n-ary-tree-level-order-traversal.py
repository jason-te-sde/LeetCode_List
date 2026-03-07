"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if root is None:
            return res
        
        q = deque([root])

        while q:
            sz = len(q)
            level = []
            for i in range(sz):
                cur = q.popleft()
                level.append(cur.val)
                for child in cur.children:
                    q.append(child)
            res.append(level)
        return res
        