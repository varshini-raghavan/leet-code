# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        def check(root):
            if root is None:
                return
            lst.append(root.val)
            check(root.left)
            check(root.right)
        check(root)
        return lst
        