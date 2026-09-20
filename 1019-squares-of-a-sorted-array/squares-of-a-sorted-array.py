class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        i=0
        j= len(nums)-1
        k= len(nums)-1

        output = [0]*len(nums)  #important point to note
        while i <= j:
            if nums[i]**2 < nums[j]**2:
                output[k] = nums[j]**2
                j -= 1
            else:
                output[k] = nums[i]**2
                i += 1
            k -= 1
        return output
         
 