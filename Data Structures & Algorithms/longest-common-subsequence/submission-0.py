class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.rows = len(text1)
        self.cols = len(text2)
        self.memo = [[-1] * self.cols for i in range(self.rows)]
        self.seq = 0
        def dp(r, c):
            if r == self.rows or c == self.cols:
                return 0
            if self.memo[r][c] > 0:
                return self.memo[r][c]
            if text1[r] == text2[c]:
                return 1 + dp(r+1,c+1)
            
            self.memo[r][c] = max(dp(r+1,c), dp(r,c+1))
            return self.memo[r][c]
        return dp(0,0)

        