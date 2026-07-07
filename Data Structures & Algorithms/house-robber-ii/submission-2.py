class Solution:
    def rob(self, nums: List[int]) -> int:
        def getMax(nums):
            dp = [0]*len(nums)
            
            if nums == []:
                return 0

            if len(nums) < 2:
                return max(nums)
            
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            for i in range(2, len(dp)):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            return dp[-1]
    
        if len(nums) == 1:
            return nums[0]
        return max(getMax(nums[1:]), getMax(nums[:len(nums)-1]))