# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode, past=set()) -> ListNode:
        if head == None: return None
        if head in past: return head
        past.add(head)
        return self.detectCycle(head.next, past)

#### O(n), O(n); 8, 100 Python3
#### TODO