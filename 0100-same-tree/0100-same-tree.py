# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node, values):
            if not node:
                values.append(None)
                return values
            else:
                values.append(node.val)
                return dfs(node.left, values) and dfs(node.right, values)
        return dfs(p, []) == dfs(q, [])