# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, left_len: int, right_len: int, max_len: int) -> int:
            if not node:
                return max_len
            max_len = max(max_len, left_len, right_len)
            return max(
                dfs(node.left, 0, left_len + 1, max_len),
                dfs(node.right, right_len + 1, 0, max_len),
            )
        return dfs(root, 0, 0, 0)