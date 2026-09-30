class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        f = {0: 1}
        count = 0
        total = 0

        for i in range(len(nums)):

            total += nums[i]
            remainder = total % k
            count += f.get(remainder,0) 
            f[remainder] = f.get(remainder, 0) + 1                          
        
        return count