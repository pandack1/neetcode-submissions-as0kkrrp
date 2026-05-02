class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        L = 0
        length = -1
        window = set()

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            length = max(R-L+1, length) 

        return length
