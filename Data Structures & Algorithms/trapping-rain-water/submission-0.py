class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        for i in range(len(height)):
            greater_left, greater_right = 0, 0
            for j in range(0,i):
                if height[j] > height[i]:
                    greater_left = max(greater_left, height[j])
            for k in range(i+1,len(height)):
                if height[k] > height[i]:
                    greater_right = max(greater_right, height[k])
            if greater_left > 0 and greater_right > 0:
                total_water += min(greater_left, greater_right) - height[i]
        
        return total_water
            
            
                
        