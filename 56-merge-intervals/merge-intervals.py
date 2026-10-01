class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []
        intervals.sort()
        
        start_1 = intervals[0][0]
        end_1 = intervals[0][1]

        for i in range(1,len(intervals)):
            start_2 = intervals[i][0]
            end_2 = intervals[i][1]

            if end_1 >= start_2: # OVERLAP
                end_1 = max(end_1,end_2)
                continue
            
            result.append([start_1,end_1]) #NO OVERLAP

            start_1 = start_2
            end_1 = end_2
        
        result.append([start_1,end_1])

        return result 


        