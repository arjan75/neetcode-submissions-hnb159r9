class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 0
        length = len(s)
        seen = set()

        maxLength = 0
        while right < length:
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            maxLength = max(maxLength, right-left+1)
            right += 1
        return maxLength        