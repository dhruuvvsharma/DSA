class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        low = 0
        high = 0 
        
        subarr_final_len = float('inf')
        total_rn = 0 
##HIRE
        while high < len(nums):
            total_rn += nums[high]

            while total_rn >= target:
                subarr_len = (high - low)+ 1    ##important 
                subarr_final_len = min(subarr_len,subarr_final_len)
##FIRE
                total_rn -= nums[low]
                low +=1 
            
            high +=1

        if subarr_final_len == float('inf'):
            return 0
        else:
            return subarr_final_len

