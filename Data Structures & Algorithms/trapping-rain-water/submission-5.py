class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        left_max, right_max = height[L], height[R]
        total_water = 0

        while L<R:
            if left_max < right_max:
                total_water += min(left_max, right_max) - height[L]
                L += 1
                left_max = max(left_max, height[L])
            else:
                total_water += min(left_max, right_max) - height[R]
                R -= 1
                right_max = max(right_max, height[R])
            
        return total_water
            


        