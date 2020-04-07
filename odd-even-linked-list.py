# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None: return head
        # Initialize vars
        odd = head
        even = head.next
        first_even = even
        # loop until end (either is None) while changing nexts
        while True:
            if even.next == None:
                break
            elif even.next.next == None:
                odd.next = odd.next.next
                odd = odd.next
                even.next = None
                break
            else:
                # change nexts
                odd.next = odd.next.next
                even.next = even.next.next
                # change pointers
                odd = odd.next
                even = even.next
        # point last odd -> first even
        odd.next = first_even
        return head
#### O(n), O(1); 52, 8 Python3
# CONCISE