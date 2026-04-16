class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(num):
            if num == n:
                return 1
            if num > n:
                return 0
            if num in cache:
                return cache[num]
            cache[num] = dfs(num+1) + dfs(num+2)
            return cache[num]

        return dfs(0)
        