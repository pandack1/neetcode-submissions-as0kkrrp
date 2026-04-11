class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0
        self.grid = grid
        self.r_count, self.c_count = len(grid), len(grid[0])

        for r, row in enumerate(self.grid):
            for c, value in enumerate(row):
                if value == "1":
                    self.count += 1
                    self.dfs(r,c)
        
        return self.count


    def dfs(self, r, c):
        if min(r,c) < 0 or r == self.r_count or c == self.c_count or self.grid[r][c] == "0":
            return
        
        self.grid[r][c] = "0"

        self.dfs(r+1,c)
        self.dfs(r-1,c)
        self.dfs(r,c+1)
        self.dfs(r,c-1)
        

        