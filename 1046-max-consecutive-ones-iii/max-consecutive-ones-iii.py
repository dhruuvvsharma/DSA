class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0 
        maximum_zero = 0
        longest = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                maximum_zero += 1

            while maximum_zero > k:
                if nums[left] == 0:
                    maximum_zero -= 1
                
                left += 1
            longest = max(longest , right - left + 1)

        return longest
        