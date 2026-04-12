class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            if target >= matrix[i][0] and target <= matrix[i][cols-1]:
                targetRow = i 
                start = 0
                end = cols-1

                while start <= end:
                    middle = (start + end)//2

                    if matrix[targetRow][middle] == target:
                        return True
                    
                    elif matrix[targetRow][middle] > target:
                        end = middle - 1
                    
                    else:
                        start = middle + 1
        return False
                    

        