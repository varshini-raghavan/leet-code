# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode, currentSum: int = 0) -> int:
        if root is None:
            return 0
        currentSum = currentSum * 10 + root.val
        if root.left is None and root.right is None:
            return currentSum
        return self.sumNumbers(root.left, currentSum) + self.sumNumbers(root.right, currentSum)