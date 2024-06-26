# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder=[]
        def inord(root):
            if not root:
                return
            inord(root.left)
            inorder.append(root.val)
            inord(root.right)
        inord(root)
        diff=float("inf")
        for i in range(len(inorder)-1):
            diff=min(diff,abs(inorder[i]-inorder[i+1]))
        return diff