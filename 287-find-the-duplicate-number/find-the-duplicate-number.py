class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = 0
        fast = 0

        while True: # Cycle in array
            slow = nums[slow]  #1x
            fast = nums[nums[fast]]  ##2x
            

            if slow == fast:
                slow = 0
                
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow
        