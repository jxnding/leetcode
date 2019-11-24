# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        curr = ans
        carry = 0
        while l1 or l2:
            # Assign
            a, b = 0, 0
            if l1: 
                a = l1.val
                l1 = l1.next
            if l2: 
                b = l2.val
                l2 = l2.next
            # Sum and carry
            s = a+b+carry
            carry = 0
            if s>=10:
                carry = 1
                s -= 10
            # Store
            curr.next = ListNode(s)
            curr = curr.next
        if carry==1:
            curr.next = ListNode(1)
        return ans.next
#### O(n), O(n); 45, 12
#### Below is my solution for O(1) storage; 25, 36
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        curr = ans
        carry = 0
        while l1 or l2:
            # Assign
            a, b = 0, 0
            if l1: a = l1.val
            if l2: b = l2.val
            # Sum and carry
            s = a+b+carry
            carry = 0
            if s>=10:
                carry = 1
                s -= 10
            # Store using list, so O(1)
            if l2:
                l2 = l2.next
            if l1:
                l1.val = s
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = ListNode(s)
                curr = curr.next
        if carry==1:
            curr.next = ListNode(1)
        return ans.next