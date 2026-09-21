class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_result = nums[0]+nums[1]+ nums[len(nums)-1]
        
        for i in range(len(nums)-2):
            j= i + 1
            k =len(nums) -1 
            total = target - nums[i]

            while j < k :
                s = nums[j]+ nums[k]
                sum_till_now= s + nums[i]
                
                #only this code is different from previous 
                if abs(sum_till_now - target) < abs(closest_result - target):
                    closest_result = sum_till_now

                
                if s == total:
                    return target

                if s < total:
                    j += 1
                else:   ## s > total
                    k -= 1
        
        return closest_result


        