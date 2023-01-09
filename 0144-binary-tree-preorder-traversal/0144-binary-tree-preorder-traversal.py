# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traversal(node, added):
            if not node: return added
            added.append(node.val)
            return traversal(node.left, added) and traversal(node.right, added)
        return traversal(root, ans)
                                                            