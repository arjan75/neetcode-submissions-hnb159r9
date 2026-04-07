class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0 

        if len(nums) <= 2:
            return max(nums)

        profits = [0]*len(nums)
        profits[0] = nums[0]
        profits[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            profits[i] = max(profits[i-1], profits[i-2] + nums[i])
        return profits[-1]
        