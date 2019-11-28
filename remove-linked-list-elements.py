# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#>>> a = ListNode(1)
#>>> a.next = ListNode(2)
#>>> a.next.next = ListNode(6)
#>>> a.next.next.next = ListNode(3)
#>>> a.next.next.next.next = ListNode(4)
#>>> a.next.next.next.next.next = ListNode(5)
#>>> a.next.next.next.next.next.next = ListNode(6)

# Solution
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        dummy = ListNode(-1)
        dummy.next = head

        curr = dummy
        while curr is not None and curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
        
# My solution (in-place)
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return
        while head.val == val:
            head = head.next
            if head is None:
                break

        curr = head
        if curr is None:
            return
        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
            if curr is None:
                break
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
