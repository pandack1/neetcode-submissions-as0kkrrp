class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.image = image
        self.start_color = image[sr][sc]
        self.rows, self.cols = len(image), len(image[0])
        if self.start_color == color:
            return self.image
        self.dfs(self.image, sr, sc, color)
        return self.image

    def dfs(self, image, sr, sc, color):
        if min(sr,sc) < 0 or sr == self.rows or sc == self.cols or self.start_color != image[sr][sc]:
            return
        
        image[sr][sc] = color
        self.dfs(image, sr+1, sc, color)
        self.dfs(image, sr-1, sc, color)
        self.dfs(image, sr, sc+1, color)
        self.dfs(image, sr, sc-1, color)
        return
        
        

        