class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        if left == sum(nums) - nums[0]:  #Edge CASE
            return 0
        else:
            for i in range(1,len(nums)):
                left = left + nums[i-1]
                right = sum(nums) - nums[i] - left 

                if left == right:
                    return i
        
            return -1 


        