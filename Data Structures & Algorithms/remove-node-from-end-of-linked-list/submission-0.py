# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        haha = res
        for i in range(n):
            head = head.next
        while head:
            head = head.next
            haha = haha.next
        haha.next = haha.next.next
        return res.next