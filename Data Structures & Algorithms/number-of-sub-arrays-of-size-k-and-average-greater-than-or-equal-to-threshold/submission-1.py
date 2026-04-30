class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        sum = 0
        L = 0
        sub = 0
        for R in range(len(arr)):
            if R-L+1 > k:
                sum = sum - arr[L]
                L += 1

            sum = sum + arr[R]

            if sum >= threshold * k and R - L + 1 == k:
                sub += 1 

        return sub
        