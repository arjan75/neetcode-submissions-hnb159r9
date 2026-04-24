class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        length = len(nums)
        dp = [1]*length
        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

        