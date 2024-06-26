# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder=[]
        def inord(root):
            if not root:
                return
            inord(root.left)
            inorder.append(root.val)
            inord(root.right)
        inord(root)
        inorder.sort
        return inorder[k-1]