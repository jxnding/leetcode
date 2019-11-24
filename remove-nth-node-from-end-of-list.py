# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        second = head
        for _ in range(n):
            second = second.next
        if second == None: # If n = length of list, skip head
            return head.next
        while second.next:
            second = second.next
            first = first.next
        first.next = first.next.next
        return head

# O(n), 1 pass!
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions