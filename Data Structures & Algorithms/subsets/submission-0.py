class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtrack(index, currentPath):
            if index == len(nums):
                answer.append(currentPath[:])
                return
            
            currentPath.append(nums[index])
            backtrack(index+1, currentPath)
            currentPath.pop()
            backtrack(index+1, currentPath)
        
        backtrack(0, [])
        return answer

        
        