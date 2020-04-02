# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        def mid_node(first, second):
            if second==None or second.next==None:
                return first
            return mid_node(first.next, second.next.next)
        if head==None: return None
        if head.next==None: return head
        return mid_node(head, head)

#### O(n), O(1); 13, 7 Python3
# Review: cleaner code