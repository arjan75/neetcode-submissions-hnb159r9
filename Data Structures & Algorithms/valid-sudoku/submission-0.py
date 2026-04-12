class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        acceptedSet = set()
        for i in range(1, 10):
            acceptedSet.add(str(i))
        
        acceptedSet.add(".")

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in seen or board[i][j] not in acceptedSet:
                    return False
                seen.add(board[i][j])
            
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue

                if board[j][i] in seen or board[j][i] not in acceptedSet:
                    return False
                seen.add(board[j][i])
        
        startPoints = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        for point in startPoints:
            seen = set()
            for i in range(0, 3):
                for j in range(0, 3):
                    curPointX = point[0] + i
                    curPointY = point[1] + j

                    if board[curPointX][curPointY] == ".":
                        continue

                    if board[curPointX][curPointY] in seen or board[curPointX][curPointY] not in acceptedSet:
                        return False
                    seen.add(board[curPointX][curPointY])
            
        return True


                    


        