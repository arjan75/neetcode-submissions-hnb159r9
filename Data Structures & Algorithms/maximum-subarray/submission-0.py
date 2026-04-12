class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMaxSum = float('-inf')
        localMaxSum = float('-inf')

        for num in nums:
            localMaxSum = max(num, localMaxSum+num)
            globalMaxSum = max(globalMaxSum, localMaxSum)
        return globalMaxSum
        