class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seenSet = set()
        for num in nums:
            seenSet.add(num)


        maxLength = 0
        for num in nums:
            if num-1 not in seenSet:
                i = num
                while i in seenSet:
                    i += 1
                maxLength = max(maxLength, i-num)
        return maxLength



        