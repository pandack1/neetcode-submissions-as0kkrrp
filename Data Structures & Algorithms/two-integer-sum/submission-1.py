class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if (target - num) not in num_map:
                num_map[num] = i
            else:
                return [num_map[target - num], i]


        