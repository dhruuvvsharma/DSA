class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        no_deletion = arr[0]
        deletion = float('-inf') #No Significance 
        result = arr[0]

        for i in range(1,len(arr)):
            v1= arr[i] #cut
            v2 = no_deletion + arr[i] #carry

            best_no_deletion = max(v1,v2)

            
            v3 = deletion + arr[i] ## Deletion already used 
            v4 = no_deletion #Delete Current arr[i]

            best_deletion = max(v3,v4)


        ##UPDATE
            no_deletion  = best_no_deletion
            deletion =  best_deletion
            result = max(result,no_deletion,deletion)         
        
        return result 




