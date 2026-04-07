class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setOfNums = set()
        for i in nums:
            if i in setOfNums:
                return True
            setOfNums.add(i)
        return False
        