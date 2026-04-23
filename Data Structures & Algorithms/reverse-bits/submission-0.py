class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0

        while i < 32:
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
            i += 1
        
        return res
        