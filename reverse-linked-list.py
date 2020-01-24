class Solution:
    def reverseList(self, head: ListNode, prev=None) -> ListNode:
        if head==None: return None
        if head.next==None:
            head.next = prev
            return head
        next = head.next
        head.next = prev
        prev = head
        return self.reverseList(next, prev)
#### O(n), O(1); Python3 8,22 (48, 18.5); Python2 5, 5 (64, 18.4)
