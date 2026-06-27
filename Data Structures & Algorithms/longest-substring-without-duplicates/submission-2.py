class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        left = 0
        right = 0

        if len(s) < 2:
            return len(s)

        maxLength = 0
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxLength = max(maxLength, right-left+1)
            right += 1
        return maxLength 




        