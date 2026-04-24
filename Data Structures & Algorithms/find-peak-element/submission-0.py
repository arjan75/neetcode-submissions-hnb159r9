class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        length = len(nums)
        while start <= end:
            middle = (start + end) // 2
            if middle > 0 and nums[middle-1] > nums[middle]:
                end = middle-1
            
            elif middle+1 < length and nums[middle+1] > nums[middle]:
                start = middle+1
            
            else:
                return middle
        