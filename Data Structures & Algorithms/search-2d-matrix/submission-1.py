class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bot = m-1

        while top<=bot:

            middle_row = (top+bot)//2
            print(middle_row)
            if matrix[middle_row][0] == target or matrix[middle_row][-1] == target:
                return True
            

            if matrix[middle_row][0] > target:
                bot = middle_row - 1
            elif matrix[middle_row][-1] < target:
                top = middle_row + 1
            else:
                break

        print(middle_row)
        l = 0
        r = n-1

        while l<=r:

            mid = (l+r)//2
            if target == matrix[middle_row][mid]:
                return True
            elif target > matrix[middle_row][mid]:
                l = mid+1
            else:
                r = mid-1

        return False
            

