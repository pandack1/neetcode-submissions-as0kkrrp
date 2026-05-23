class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 1, len(nums)

        while L < R:
            if nums[L-1] == nums[L]:
                nums.pop(L)
                R -= 1
            else:
                L += 1

        return len(nums)