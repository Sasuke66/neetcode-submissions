# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
        dummy = prev = ListNode(0)
        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            prev.next = node
            prev = prev.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        return dummy.next