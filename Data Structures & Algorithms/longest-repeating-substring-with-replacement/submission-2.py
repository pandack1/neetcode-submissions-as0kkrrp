class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        length = 0
        freq = {}
        max_f = 0

        for R in range(len(s)):
            freq[s[R]] = freq.get(s[R], 0) + 1
            max_f = max(max_f, freq[s[R]])

            if (R - L + 1) - max_f > k:
                freq[s[L]] -= 1
                L += 1
            
            length = max(length, R - L + 1)

        return length