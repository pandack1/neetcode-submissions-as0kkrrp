class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.rows = len(obstacleGrid)
        self.cols = len(obstacleGrid[0])
        self.cache = [[0] * self.cols for i in range(self.rows)]
        self.grid = obstacleGrid

        def memoization(r, c):
            if r == self.rows or c == self.cols or self.grid[r][c] == 1:
                return 0
            if self.cache[r][c] > 0:
                return self.cache[r][c]
            if r == self.rows-1 and c == self.cols-1:
                return 1

            self.cache[r][c] = memoization(r+1, c) + memoization(r, c+1)

            return self.cache[r][c]

        return memoization(0,0)

        