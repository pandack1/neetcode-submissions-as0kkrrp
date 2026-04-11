class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] > nums[i-1]:
                i += 1
            else:
                for j in range(i+1, len(nums)):
                    nums[j-1] = nums[j]
                nums.pop()
        return len(nums)