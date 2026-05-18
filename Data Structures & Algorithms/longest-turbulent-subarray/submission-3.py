class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        L = 0
        comaprison = 0
        temp = arr[0]

        def get_sign(a, b):
            if a < b: return "<"
            if a > b: return ">"
            return "="
        prev_sign = "="
        for R in range(1, len(arr)):
            sign = get_sign(arr[R-1], arr[R])
            if sign == "=":
                L = R
            elif sign == prev_sign:
                L = R-1
            prev_sign = sign
            res = max(R-L+1, res)

        return res 
        