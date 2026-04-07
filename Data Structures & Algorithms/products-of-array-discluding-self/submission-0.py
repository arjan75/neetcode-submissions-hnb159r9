class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftSide = [1]*len(nums)
        rightSide = [1]*len(nums)

        i = len(nums)-1
        runningSum = 1
        while i >= 0:
            rightSide[i] = runningSum
            runningSum = runningSum*nums[i]
            i -= 1
        
        runningSum = 1
        for i in range(len(nums)):
            leftSide[i] = runningSum
            runningSum = runningSum*nums[i]
        
        for i in range(len(nums)):
            nums[i] = leftSide[i]*rightSide[i]
        
        return nums



        