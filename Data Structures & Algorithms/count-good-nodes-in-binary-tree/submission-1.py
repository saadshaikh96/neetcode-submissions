# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countGood(root, root.val)

    def countGood(self, node, maxSeen):
        if not node:
            return 0
        numGood = int(node.val >= maxSeen)
        maxSeen = max(maxSeen, node.val)
        numGood += self.countGood(node.left, maxSeen)
        numGood += self.countGood(node.right, maxSeen)
        return numGood