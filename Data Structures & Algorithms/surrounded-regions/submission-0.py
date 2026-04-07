class Solution:
    def solve(self, board: List[List[str]]) -> None:
        length = len(board)
        breadth = len(board[0])

        def markBoundaries(i, j, target):
            if i < 0 or j < 0 or i >= length or j >= breadth or board[i][j] != "O":
                return 
            
            board[i][j] = target
            markBoundaries(i+1, j, target)
            markBoundaries(i-1, j, target)
            markBoundaries(i, j+1, target)
            markBoundaries(i, j-1, target)  

        for i in range(length):
            for j in range(breadth):
                if (i == 0 or j == 0 or i == length-1 or j == breadth-1) and board[i][j] == "O":
                    markBoundaries(i, j, "T")
    
        for i in range(length):
            for j in range(breadth):
                if board[i][j] == "O":
                    markBoundaries(i, j, "X")

        for i in range(length):
            for j in range(breadth):
                if board[i][j] == "T":
                    board[i][j] = "O"
        

        