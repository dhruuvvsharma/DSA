class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        min_ending = nums[0]
        max_ending = nums[0]
        result = abs(nums[0])

        for i in range(1,len(nums)):
           
            v1= nums[i]
            v2 = max_ending + nums[i]
            v3 = min_ending + nums[i]

            max_ending = max(v1,v2,v3)
            min_ending = min(v1,v2,v3)
            result = max(result, max_ending, abs(min_ending))
        
        return result 