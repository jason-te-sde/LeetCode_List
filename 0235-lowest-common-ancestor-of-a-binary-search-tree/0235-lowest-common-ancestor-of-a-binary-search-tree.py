# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            Tag: Iteration
            Time complexity: O(h)
            Space complexity: O(1)
        """
        cur = root
        while cur:
            if max(p.val, q.val) < cur.val:
                cur = cur.left
            elif min(p.val, q.val) > cur.val:
                cur = cur.right
            else:
                return cur