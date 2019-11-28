# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def merge(ans):
            nonlocal l1
            nonlocal l2
            if l1==None and l2==None:
                return ans
            elif l1==None:
                ans.next = l2
                l2 = l2.next
            elif l2==None:
                ans.next = l1
                l1 = l1.next
            else:
                if l1.val<l2.val:
                    ans.next = l1
                    l1 = l1.next
                else:
                    ans.next = l2
                    l2 = l2.next
            return merge(ans.next)
        head = ListNode(0)
        ans = merge(head)
        return head.next
#### O(n), O(1)
#### Should use while l1 and l2:
#### https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).

# Previous solution 11/5/19, cleaner but has non-tail recursion

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None and l2==None: #just in case
            return None
        #Base cases
        if l1==None:
            return l2
        if l2==None:
            return l1
        
        if l1.val>l2.val:
            curr = l2
            curr.next = self.mergeTwoLists(l1, l2.next)
            return curr
        else:
            curr = l1
            curr.next = self.mergeTwoLists(l1.next, l2)
            return curr