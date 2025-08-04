# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        global flag
        flag = True

        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]):
            global flag

            if p and q and p.val == q.val:
                dfs(p.left, q.left)
                dfs(p.right, q.right)
            elif not p and not q:
                return
            else:
                flag = False
                return

        dfs(p,q)

        return flag

                



