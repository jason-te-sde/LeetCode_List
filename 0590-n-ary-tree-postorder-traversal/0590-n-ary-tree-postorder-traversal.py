"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []
        self.traversal(root)
        return self.res
    
    def traversal(self, root: 'Node') -> None:
        if root is None:
            return 
        for child in root.children:
            self.traversal(child)
        self.res.append(root.val)