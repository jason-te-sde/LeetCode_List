"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        self.traverse(root)
        return self.res
    
    def traverse(self, root: 'Node') -> None:
        if root is None:
            return
        self.res.append(root.val)
        for child in root.children:
            self.traverse(child)
        