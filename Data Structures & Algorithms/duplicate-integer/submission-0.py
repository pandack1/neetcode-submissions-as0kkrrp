class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = {}
        for num in nums:
            if num not in count_map:
                count_map[num] = 1
            else:
                return True
        return False
        