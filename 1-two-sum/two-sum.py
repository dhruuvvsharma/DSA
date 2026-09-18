class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        _dict = {}
        for i in range (len(nums)):
            num = nums[i]
        
            needed = target - num  
            if needed in _dict:
                return [_dict[needed],i]

            _dict[num]= i  
