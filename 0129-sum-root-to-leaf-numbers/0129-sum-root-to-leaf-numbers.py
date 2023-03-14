# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root):
        def helper(sum, root):
            if not root:
                return 0   
            sum = sum * 10 + root.val
            if not root.left and not root.right:
                return sum
            return helper(sum, root.left) + helper(sum, root.right)

        return helper(0, root)