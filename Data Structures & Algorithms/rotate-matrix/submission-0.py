class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        

        m = len(matrix)
        n = len(matrix[0])

        #tran = [[0] * m for _ in range(n)]


        for i in range(m):
            for j in range(i+1, n):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

                

        for row in matrix:

            l = 0
            r = len(row) - 1

            while l < r:

                row[l],row[r] = row[r],row[l]
                l += 1
                r -= 1

        

