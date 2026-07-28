class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counters = [0]*26
        left = 0
        right = 0
        longest = 0
        while right < len(s):
            counters[ord(s[right])-65] += 1

            while right-left+1-max(counters) > k:
                counters[ord(s[left])-65] -= 1
                left += 1
            
            longest = max(longest, right-left+1)
            right += 1
        return longest


        