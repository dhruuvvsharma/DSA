class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left = 0 
        right = 0
        max_avg = float('-inf')
        avg_till_now = 0

        for right in range(len(nums)):
            avg_till_now += nums[right] / k

            if (right - left + 1) > k:
                avg_till_now -= nums[left] / k
                left +=1

            if (right - left + 1) == k:
                max_avg = max(max_avg,avg_till_now)

        return max_avg    



