# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        if l1==None and l2==None:
            if carry==0:
                return None
            return ListNode(carry)
        if l1==None:
            sum = l2.val+carry
            l2 = l2.next
        elif l2==None:
            sum = l1.val+carry
            l1 = l1.next
        else:
            sum = l1.val+l2.val+carry
            l1, l2 = l1.next, l2.next
        
        if sum>=10:
            carry = 1
            sum = sum-10
        else:
            carry = 0
        
        digit = ListNode(sum)
        digit.next = self.addTwoNumbers(l1, l2, carry)
        return digit