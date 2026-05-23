class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        hash_dict = {}
        for r in range(len(nums)):
            if r > 0:
                hash_dict[nums[r]] = hash_dict.get(nums[r], 0) + 1
                if nums[r] != nums[r-1]:
                    nums[l] = nums[r]
                    l += 1
                elif nums[r] == nums[r-1] and hash_dict[nums[r]] == 2:
                    nums[l] = nums[r]
                    l += 1
            else:
                hash_dict[nums[r]] = hash_dict.get(nums[r], 0) + 1
        return l
                    
            