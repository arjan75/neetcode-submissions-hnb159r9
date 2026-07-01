class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length = len(board)
        breath = len(board[0])

        visited = set()
        def traverse(i, j, index):
            if index == len(word):
                return True

            if i < 0 or i >= length or j < 0 or j >= breath or board[i][j] != word[index] or (i, j) in visited:
                return False

            visited.add((i, j))
            value = traverse(i+1, j, index+1) or traverse(i-1, j, index+1) or traverse(i, j-1, index+1) or traverse(i, j+1, index+1)
            visited.remove((i, j))
            return value

        if word == "" or not board:
            return False
        

        for i in range(length):
            for j in range(breath):
                if board[i][j] == word[0]:
                    if traverse(i, j, 0):
                        return True
        return False


            
            
            



        