class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def cycle(i, j):
            nonlocal matrix
            temp = matrix[i][j]
            matrix[i][j] = matrix[len(matrix)-j-1][i]
            matrix[len(matrix)-j-1][i] = matrix[len(matrix)-i-1][len(matrix)-j-1]
            matrix[len(matrix)-i-1][len(matrix)-j-1] = matrix[j][len(matrix)-i-1]
            matrix[j][len(matrix)-i-1] = temp
        
        for i in range(len(matrix)//2):
            for j in range(i, len(matrix[i])-i-1):
                cycle(i, j)
#### SNIPED
#### O(n^2), O(1); 73, 100 Python3
