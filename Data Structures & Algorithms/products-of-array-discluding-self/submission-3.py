class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        ele_zero = []
        prod = 1
        prod_zero = False
        for i,n in enumerate(nums):
            if n!=0:
                prod *= n
            else:
                ele_zero.append(i)
                prod_zero = True

        
        temp = 1
        for i,num in enumerate(nums):
            if num != 0 and prod_zero == True:
                res.append(0)
            elif num != 0 and prod_zero == False:
                temp = prod/num
                res.append(int(temp))
            else:
                if len(ele_zero) > 1:
                    res.append(0)
                else:
                    temp = prod
                    res.append(int(temp))

        
        return res
