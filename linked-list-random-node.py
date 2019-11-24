# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
class Solution:

    def __init__(self, head: ListNode):
        self.head = head
        self.ans = None
        
    def getRandom(self) -> int:
        n = 1
        ans = None
        head = self.head
        while head.next:
            if random.random()<1/n:
                ans = ListNode(head.val)
            head = head.next
            n+=1
        return ans
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()