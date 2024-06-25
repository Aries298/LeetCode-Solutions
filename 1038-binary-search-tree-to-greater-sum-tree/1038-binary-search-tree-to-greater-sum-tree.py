class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        ans=0
        def helper(node):
            nonlocal ans
            if node==None:
                return
            helper(node.right)
            ans+=node.val
            node.val=ans
            helper(node.left)
        helper(root)  
        return root  