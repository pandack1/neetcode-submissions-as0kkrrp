class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) # total rows
        n = len(obstacleGrid[0]) # total cols

        if(obstacleGrid[m-1][n-1] == 1):
            return 0

        prevRow = [0] * n
        
        for r in range(m-1,-1,-1):
            currRow = [0] * n

            for c in range(n-1,-1,-1):
                if r == m-1 and c == n-1:
                    currRow[c] = 1
                elif obstacleGrid[r][c] == 1:
                    currRow[c] = 0
                elif c == n-1:
                    currRow[c] = prevRow[c]
                else:
                    currRow[c] = currRow[c+1] + prevRow[c]
            prevRow = currRow

        return prevRow[0]
        