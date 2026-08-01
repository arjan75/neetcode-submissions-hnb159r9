class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i]-1 not in setOfNums:
                k = nums[i]
                while k in setOfNums:
                    k += 1
                longest = max(longest, k-nums[i])
        return longest

                
                
                


        
