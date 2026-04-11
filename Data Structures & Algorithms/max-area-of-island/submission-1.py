class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.r_count, self.c_count = len(grid), len(grid[0])
        self.max_area = 0

        for r, row in enumerate(self.grid):
            for c, value in enumerate(row):
                if value == 1:
                    self.count = 0
                    self.dfs(r,c)
                    self.max_area = max(self.max_area, self.count)
        
        return self.max_area


    def dfs(self, r, c):
        if min(r,c) < 0 or r == self.r_count or c == self.c_count:
            return
        
        elif self.grid[r][c] == 0:
            return

        
        self.grid[r][c] = 0
        self.count += 1

        self.dfs(r+1,c)
        self.dfs(r-1,c)
        self.dfs(r,c+1)
        self.dfs(r,c-1)
        