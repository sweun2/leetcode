# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global sumv
        global flag
        flag = False
        sumv = 0 if not root else root.val
        def dfs(tree):
            global sumv
            global flag

            if tree == None:
                return
            if sumv == targetSum and not tree.left and not tree.right:
                flag = True
                return
            if tree.left:
                sumv += tree.left.val
                dfs(tree.left)
                sumv -= tree.left.val
            
            if tree.right:
                sumv += tree.right.val
                dfs(tree.right)
                sumv -= tree.right.val
            
        dfs(root)
        return flag