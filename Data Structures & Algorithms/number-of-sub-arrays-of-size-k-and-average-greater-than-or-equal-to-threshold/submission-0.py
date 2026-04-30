class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        window = []
        L = 0
        sub = 0
        for R in range(len(arr)):
            if R-L+1 > k:
                window.remove(arr[L])
                L += 1
            window.append(arr[R])

            if(len(window)) < k:
                continue

            win_avg = sum(window)/len(window)
            if win_avg < threshold:
                continue
            sub += 1 

        return sub
        