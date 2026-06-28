class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        prefixSum = { 0: 1 }
        curSum = 0
        numberOfSubArrays = 0
        for i in range(len(nums)):
            curSum += nums[i]

            if curSum-k in prefixSum:
                numberOfSubArrays += prefixSum[curSum-k]
            
            if curSum in prefixSum:
                prefixSum[curSum] += 1
            else:
                prefixSum[curSum] = 1
        return numberOfSubArrays

            

            



        