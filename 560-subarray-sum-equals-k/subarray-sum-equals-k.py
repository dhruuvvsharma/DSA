class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        f = {0:1} #hashmap
        count = 0 #no. of subarrays
        total = 0

        for i in range(len(nums)):

            total += nums[i]
            count += f.get( total - k , 0) 
            f[total] = f.get( total , 0) + 1

        return count  

            
