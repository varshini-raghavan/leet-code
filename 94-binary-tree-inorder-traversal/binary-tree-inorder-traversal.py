# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        def check(root):
            if root is None:
                return
            check(root.left)
            lst.append(root.val)
            check(root.right)
        check(root)
        return lst
        