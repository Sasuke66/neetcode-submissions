# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False 
        currNode = head
        startNode = head.next
        while startNode != None and startNode.next != None:
            if currNode == startNode:
                return True
            currNode = currNode.next
            startNode = startNode.next.next
        return False 