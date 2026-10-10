class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        result =[-1]*len(nums)

        for i in range(len(nums)-2,-1,-1):  #intial stack ready karo!! #preloading
            stack.append(nums[i])

        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            
            if stack:
                result[i] = stack[-1]
            else:
                result[i] = -1
            
            stack.append(nums[i])
        
        return result 



        
        