class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length = len(board)
        breadth = len(board[0])
        
        visited = set()
        def traverse(i, j, index):
            if index == len(word):
                return True

            if i < 0 or j < 0 or i >= length or j >= breadth or (i, j) in visited or board[i][j] != word[index]:
                return False
            
            visited.add((i, j))
            result = traverse(i, j+1, index+1) or traverse(i, j-1, index+1) or traverse(i+1, j, index+1) or traverse(i-1, j, index+1)
            visited.remove((i, j))
            return result
        

        for i in range(length):
            for j in range(breadth):
                if board[i][j] == word[0]:
                    if traverse(i, j, 0):
                        return True
        return False

        