import pdb
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    ml = []

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getLength(self):
        cc = 0
        curr = self.head
        while curr:
            self.ml.append(curr.val)
            cc+=1
            curr = curr.next
        return cc

    # def getRandom(self) -> int:
    #     self.getLength()
    #     """
    #     Returns a random node's value.
    #     """
    #     done = False
    #     while not done:
    #         dli = []
    #         for i in range(len(self.ml)):
    #             if bool(random.getrandbits(1)):
    #                 dli.append(i)
    #         for e in dli:
    #             if len(self.ml)==1:
    #                 return self.ml[0]
    #             del self.ml[e]
    #     return 0
    def getRandom(self) -> int:
        self.getLength()
        """
        Returns a random node's value.
        """
        ind = random.randint(0,len(self.ml))

        return self.ml[ind]

ml = ListNode(0)
ml.next = ListNode(1)
ml.next.next = ListNode(2)
ml.next.next.next = ListNode(3)
ml.next.next.next.next = ListNode(4)
ml.next.next.next.next.next = ListNode(5)
ml.next.next.next.next.next.next = ListNode(6)

obj = Solution(ml)
pdb.set_trace()
