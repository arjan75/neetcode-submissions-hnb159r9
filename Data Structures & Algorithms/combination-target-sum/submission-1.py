class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        def buildCombination(index, currentPath, total):
            if total == target:
                answer.append(currentPath[:])
                return

            if index == len(nums) or total > target:
                return
            
            currentPath.append(nums[index])
            buildCombination(index, currentPath, total+nums[index])
            currentPath.pop()
            buildCombination(index+1, currentPath, total)

        
        buildCombination(0, [], 0)
        return answer
        