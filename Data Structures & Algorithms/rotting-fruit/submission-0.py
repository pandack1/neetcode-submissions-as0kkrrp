class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        minutes = 0

        while queue:
            rotted = False
            for _ in range(len(queue)):
                r, c = queue.popleft()
                neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in neighbors:
                    if min(r+dr,c+dc) < 0 or r+dr == rows or c+dc == cols or grid[r+dr][c+dc] == 0 or grid[r+dr][c+dc] == 2:
                        continue
                    queue.append((r+dr, c+dc))
                    fresh -= 1
                    grid[r+dr][c+dc] = 2
                    rotted = True
            if rotted:
                minutes += 1
        if fresh == 0:
            return minutes
        else:
            return -1
        
        
        
        
        

        
        