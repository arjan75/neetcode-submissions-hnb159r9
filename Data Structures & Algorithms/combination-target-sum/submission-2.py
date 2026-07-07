class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtrack(index, path, curSum):
            if curSum == target:
                answer.append(path[:])
                return 
            
            if index == len(nums) or curSum > target:
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i, path, curSum+nums[i])
                path.pop()

        backtrack(0, [], 0)
        return answer
            


        