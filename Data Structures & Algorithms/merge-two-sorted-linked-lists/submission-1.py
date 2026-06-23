# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        head = newList

        while list1 and list2:
            if list1.val < list2.val:
                newList.next = ListNode(list1.val)
                list1 = list1.next
            else:
                newList.next = ListNode(list2.val)
                list2 = list2.next

            newList = newList.next

        remaining = list1 if list1 else list2

        while remaining:
            newList.next = ListNode(remaining.val)
            newList = newList.next
            remaining = remaining.next

        return head.next