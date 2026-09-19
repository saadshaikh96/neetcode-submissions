# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        rightViewNodes = []
        queue = deque([root])
        while queue:
            numNodesAtCurrentLevel = len(queue)
            for i in range(numNodesAtCurrentLevel):
                currentNodeAtLevel = queue.popleft()
                if i == numNodesAtCurrentLevel - 1:
                    rightViewNodes.append(currentNodeAtLevel.val)
                if currentNodeAtLevel.left:
                    queue.append(currentNodeAtLevel.left)
                if currentNodeAtLevel.right:
                    queue.append(currentNodeAtLevel.right)

        return rightViewNodes