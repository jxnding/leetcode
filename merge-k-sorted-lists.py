# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        from Queue import PriorityQueue
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val, node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next
#### O(n log k), O(k)
#### Think of runtime wrt output instead of input
#### TODO: Why doesn't Python3 work?
#### below is Python3 Solution
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,(0,node)))
        while q.qsize()>0:
            curr.next = q.get()[1][1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, (0,curr.next)))
        return dummy.next