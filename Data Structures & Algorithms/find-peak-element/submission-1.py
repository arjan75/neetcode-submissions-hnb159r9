class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        start = 0
        end = length-1

        while start <= end:
            middle = (start + end) // 2

            if middle+1 < length and nums[middle] < nums[middle+1]:
                start = middle + 1
            
            elif middle -1 >= 0 and nums[middle-1] > nums[middle]:
                end = middle-1
            else:
                return middle
        