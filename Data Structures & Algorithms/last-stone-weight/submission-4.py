class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = [-num for num in stones]
        heapq.heapify(self.stones)

        while len(self.stones) > 1:
            x, y = -heapq.heappop(self.stones), -heapq.heappop(self.stones)
            if x==y:
                pass
            else:
                self.stones.append(-abs(x-y))
        if self.stones:
            return -self.stones[0]
        else:
            return 0
        