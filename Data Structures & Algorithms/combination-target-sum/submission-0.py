class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        def buildCombination(index, currentPath):
            if sum(currentPath) == target:
                answer.append(currentPath[:])
                return

            if index == len(nums) or sum(currentPath) > target:
                return
            
            currentPath.append(nums[index])
            buildCombination(index, currentPath)
            currentPath.pop()
            buildCombination(index+1, currentPath)

        
        buildCombination(0, [])
        return answer
        