# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float("-inf"), float("inf"))

    def isValid(self, node, minBound, maxBound):
        if not node:
            return True
        if node.val <= minBound or node.val >= maxBound:
            return False
        leftIsValid = self.isValid(node.left, minBound, node.val)
        rightIsValid = self.isValid(node.right, node.val, maxBound)

        return leftIsValid and rightIsValid