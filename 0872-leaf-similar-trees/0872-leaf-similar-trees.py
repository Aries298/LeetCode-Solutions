class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        return len(set(map(tuple, map(lambda root: (lambda root, func: [] if not root else ([root.val] if (not root.left and not root.right) else func(root.left, func) + func(root.right, func)))(root, (lambda root, func: [] if not root else ([root.val] if (not root.left and not root.right) else func(root.left, func) + func(root.right, func)))), (root1, root2))))) == 1