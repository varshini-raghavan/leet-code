# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def check(root,targetSum):
            if not root:
                return False
            if targetSum==root.val and root.right is None and root.left is None:
                return True
            return check(root.left,targetSum-root.val) or check(root.right,targetSum-root.val)
        return check(root,targetSum)