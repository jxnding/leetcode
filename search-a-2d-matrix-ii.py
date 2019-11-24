class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==[]: return False
        if matrix==[[]]: return False
        i, j = 0, len(matrix[0])-1 #top right corner
        while True:
            n = matrix[i][j]
            if n==target:
                return True
            elif n>target:
                j-=1
            else:
                i+=1
            
            if i==len(matrix) or j<0:
                return False
#### O(m+n), O(1)
#### WOW, that took me too long
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        import sys
        lists = matrix
        front = [0]*len(lists)
        ans = []
        finished = False
        while not finished:
            minVal, minList = sys.maxsize, None
            finished = True
            for i in range(len(lists)):
                n = front[i]
                if n < None:
                    finished = False
                    if n.val<minVal:
                        minVal = n.val
                        minList = i
            if finished:
                break
            ans.append(minVal)
            lists[minList]=lists[minList].next
        return ans