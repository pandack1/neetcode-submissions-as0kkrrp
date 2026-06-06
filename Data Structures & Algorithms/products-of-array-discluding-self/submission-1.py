class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix, suffix = [], []
        for i in range(len(nums)):
            prefix.append(product)
            product *= nums[i]
        product = 1    
        for j in range(len(nums)-1, -1, -1):
            suffix.append(product)
            product *= nums[j]

        suffix.reverse()

        res = []
        
        for i,val in  enumerate(nums):
            res.append(prefix[i]*suffix[i]) 

        return res
            

        