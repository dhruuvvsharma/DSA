class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        Zero = 0
        One = 0
        longest = 0
        f = {}

        for i in range(len(nums)):
            if nums[i] == 0:
                Zero += 1
            else:
                One += 1
            
            diff = Zero - One 
            
            if diff == 0:  #complete array
                longest = max(longest, i+1 )
                continue 
            
            elif diff not in f:
                f[diff] = i 

            else:    # diff in hashmap F
                index = f[diff]
                length = i - index 

                longest = max(longest,length)

        return longest  


