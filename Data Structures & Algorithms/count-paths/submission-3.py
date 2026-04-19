class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.cache = [[0] * n for i in range(m)]
        self.rows = m
        self.cols = n

        def memoization(r, c):
            if r == self.rows or c == self.cols:
                return 0
            if self.cache[r][c] > 0:
                return self.cache[r][c]
            if r == self.rows-1 and c == self.cols-1:
                return 1

            self.cache[r][c] = memoization(r+1, c) + memoization(r, c+1)

            return self.cache[r][c]

        return memoization(0,0)
