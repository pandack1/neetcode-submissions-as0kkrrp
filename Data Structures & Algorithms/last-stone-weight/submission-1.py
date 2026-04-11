class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = stones
        while len(self.stones) > 1:
            self.stones = sorted(self.stones)
            x, y = self.stones[-1], self.stones[-2]
            if x==y:
                self.stones.pop()
                self.stones.pop()
            else:
                self.stones.pop()
                self.stones.pop()
                self.stones.append(abs(x-y))
        if self.stones:
            return self.stones[0]
        else:
            return 0

        