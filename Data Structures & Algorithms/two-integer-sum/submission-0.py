class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for i in range(len(nums)):
            if target-nums[i] in indexMap:
                return [indexMap[target-nums[i]], i]
            else:
                indexMap[nums[i]] = i
        
        
        