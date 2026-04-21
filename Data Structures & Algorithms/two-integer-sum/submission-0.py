class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range (len(nums)):
            current=nums[i]
            diff=target-current
            if diff in seen:
                return [seen[diff],i]
            seen[current]=i
        return 1