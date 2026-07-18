class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        visited = set()
        startingColor = image[sr][sc]
        def fillPixels(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or image[i][j] != startingColor:
                return 
        
            visited.add((i, j))
            image[i][j] = color

            fillPixels(i+1, j)
            fillPixels(i-1, j)
            fillPixels(i, j+1)
            fillPixels(i, j-1)

        fillPixels(sr, sc)
        return image

        