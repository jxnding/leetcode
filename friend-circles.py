class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        ans = 0
        students = set(range(len(M)))
        
        while students: #visit all students
            s = students.pop()
            # BFS on each student
            openSet = [s]
            visited = set()
            while openSet:
                curr = openSet.pop()
                visited.add(curr)
                if curr in students: students.remove(curr) #track what student's we've visited
                for i, n in enumerate(M[curr]): #current student's neighbors
                    if n==1 and i not in visited:
                        openSet.append(i)
            ans+=1
        return ans
#### TODO: What is runtime?, O(n); 15, 77
#### Students can be used instead of visited, tho runtime does not change (gets worse in terms of ms)
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        ans = 0
        students = set(range(len(M)))
        
        while students: #visit all students
            s = students.pop()
            # BFS on each student
            openSet = [s]
            visited = set()
            while openSet:
                curr = openSet.pop()
                visited.add(curr)
                if curr in students: students.remove(curr) #track what student's we've visited
                for i, n in enumerate(M[curr]): #current student's neighbors
                    if n==1 and i not in visited:
                        openSet.append(i)
            ans+=1
        return ans