# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        first, second = head, head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second

#### Clapped in 5 min!, first try!
#### O(n) and O(1) I believe...