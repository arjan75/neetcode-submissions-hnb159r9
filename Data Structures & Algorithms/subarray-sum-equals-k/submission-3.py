class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = {0: 1}
        curSum = 0
        count = 0
        for num in nums:
            curSum += num
            if curSum - k in prefixes:
                count += prefixes[curSum-k] 
            
            if curSum in prefixes:
                prefixes[curSum] += 1
            else:
                prefixes[curSum] = 1
            
        return count
            
        