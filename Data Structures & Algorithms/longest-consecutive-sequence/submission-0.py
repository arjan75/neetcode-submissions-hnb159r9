class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numToSet = set()
        for num in nums:
            numToSet.add(num)
        
        maxLength = 0
        for num in nums:
            if num-1 not in numToSet:
                i = num
                while i in numToSet:
                    i += 1
                maxLength = max(maxLength, i-num)
        return maxLength

            



        