# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def countNode(node):
            if node:
                return 1 + countNode(node.left) + countNode(node.right)
            else:
                return 0
        return countNode(root)