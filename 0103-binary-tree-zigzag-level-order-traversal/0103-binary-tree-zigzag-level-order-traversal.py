# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = collections.deque([root])
        res = []
        even_level = False
        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if even_level:
                res.append(level[::-1])
            else:
                res.append(level)
            even_level = not even_level
        return res