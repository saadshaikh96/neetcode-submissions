# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, 0, i, node))

        dummy = ListNode(0)
        currentNode = dummy
        while heap:
            value, nodeIdx, listIdx, node = heapq.heappop(heap)

            currentNode.next = node
            currentNode = currentNode.next

            if node.next:
                heapq.heappush(heap, (node.next.val, nodeIdx + 1, listIdx, node.next))

        return dummy.next