class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = {0: 1}
        curSum = 0

        total = 0
        for num in nums:
            curSum += num

            difference = curSum - k
            if difference in prefixes:
                total += prefixes[difference]

            if curSum in prefixes:
                prefixes[curSum] += 1
            else:
                prefixes[curSum] = 1
        return total


            
        