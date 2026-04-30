class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currmax, currmin, total = 0, 0, 0
        globalmax, globalmin = nums[0], nums[0]

        for n in nums:
            currmax = max(currmax + n, n)
            currmin = min(currmin + n, n)

            globalmax = max(globalmax, currmax)
            globalmin = min(globalmin, currmin)

            total += n

        return max(globalmax, (total - globalmin)) if globalmax > 0 else globalmax
        