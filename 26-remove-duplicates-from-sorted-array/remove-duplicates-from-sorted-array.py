class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0 #officer
        j=1 #CM
        k =1 #no. of unique values

        while j < len(nums):
            if nums [j] == nums [j-1]:
                j+=1
                continue 
            # Found Unique Value
            nums[i+1]= nums[j]
            i+=1
            j+=1
            k+=1
        return k
