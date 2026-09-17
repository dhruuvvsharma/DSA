class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        answer = []
        total = 0

        for i in range (len(nums)):
            total += nums[i]
            answer.append(total)
        
        return answer 