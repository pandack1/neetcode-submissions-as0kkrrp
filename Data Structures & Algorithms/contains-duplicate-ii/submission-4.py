class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()
        i = 0

        for j in range(len(nums)):
            if j > k:
                window.remove(nums[j - k- 1])
                i += 1
            
            if nums[j] in window:
                return True
            window.add(nums[j])

        return False
        