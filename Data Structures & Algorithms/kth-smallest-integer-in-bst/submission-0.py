# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        self.inOrderTraverse(root, nodes)
        return nodes[k - 1]

    def inOrderTraverse(self, node, nodes):
        if not node:
            return

        self.inOrderTraverse(node.left, nodes)
        nodes.append(node.val)
        self.inOrderTraverse(node.right, nodes)
