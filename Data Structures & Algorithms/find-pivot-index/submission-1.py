class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        prefix_sum, postfix_sum = [], []

        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix_sum.append(total)

        total = 0
        for j in range(len(nums)-1,-1,-1):
            total += nums[j]
            postfix_sum.append(total)

        postfix_sum.reverse()

        left_sum, right_sum = 0, 0
        for k in range(len(nums)):
            if k == 0:
                left_sum = 0
                right_sum = postfix_sum[k+1]
                if left_sum == right_sum:
                    return k
            elif k > 0 and k < len(nums)-1:
                left_sum = prefix_sum[k-1]
                right_sum = postfix_sum[k+1]
                if left_sum == right_sum:
                    return k
            elif k == len(nums)-1:
                left_sum = prefix_sum[k-1]
                right_sum = 0
                if left_sum == right_sum:
                    return k

        return -1
            



            

        