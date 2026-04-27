class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validNumbers = set()
        for i in range(1, 10):
            validNumbers.add(str(i))

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen or board[i][j] not in validNumbers:
                    return False
                seen.add(board[i][j])
        

            
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue

                if board[j][i] in seen or board[j][i] not in validNumbers:
                    return False
                seen.add(board[j][i])
        
        directions = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        startPoints = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]

        for point in startPoints:
            seen = set()
            for direction in directions:
                newRow = point[0] + direction[0]
                newCol = point[1] + direction[1]

                if board[newRow][newCol] == ".":
                    continue

                if board[newRow][newCol] in seen or board[newRow][newCol] not in validNumbers:
                    return False
                
                seen.add(board[newRow][newCol])
        return True




                
        


        