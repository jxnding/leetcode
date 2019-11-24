# Definition for singly-linked list.
import pdb
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next

class Solution:
    def findLength(self, head, num=0):
        if head==None:
            return num
        return self.findLength(head.next, num+1) #tail recursion!
    
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def removeNth(prev, head, count):
            print(count)
            if head == None:
                return None
            curr = head
            if count == (length-n): #skipping NEXT one
                if n == 1:
                    prev.next = None
                    return prev
                prev.next = removeNth(head.next, head.next.next, count+1)
                return prev
            prev.next = curr.next
            curr.next = removeNth(head, head.next, count+1)
            return curr
        length = self.findLength(head)
        if length == 1: #edge case since I skip the NEXT one 
            return None
        return removeNth(head, head.next, 1)

x = ListNode(1, ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
a = Solution().removeNthFromEnd(x,1)
pdb.set_trace()