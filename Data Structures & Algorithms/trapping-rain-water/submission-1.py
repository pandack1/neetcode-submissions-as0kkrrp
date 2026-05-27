class Solution:
    def trap(self, height: List[int]) -> int:
        pref_max, suffix_max = 0, 0
        left_arr, right_arr = [], []
        total_water = 0

        for i in range(len(height)):
            pref_max = max(pref_max, height[i])
            left_arr.append(pref_max)

        for j in range(len(height)-1, -1, -1):
            suffix_max = max(suffix_max, height[j])
            right_arr.append(suffix_max)
        
        right_arr.reverse()

        for k in range(len(height)):
            if left_arr[k] > height[k] and right_arr[k] > height[k]:
                total_water += min(left_arr[k], right_arr[k]) - height[k]
        
        return total_water