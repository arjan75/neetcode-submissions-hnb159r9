from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()

        left = 0
        right = 0

        maximum = []
        while right < len(nums):
            while window and nums[window[-1]] < nums[right]:
                window.pop()
            
            window.append(right)

            if window and window[0] < left:
                window.popleft()
            
            if right + 1 >= k:
                maximum.append(nums[window[0]])
                left += 1
            
            right += 1
        return maximum



        