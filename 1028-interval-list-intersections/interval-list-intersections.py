class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i = 0
        j = 0
        result = []

        while i < len(firstList) and j < len(secondList):
            start_1 = firstList[i][0]
            end_1 = firstList[i][1]

            start_2 = secondList[j][0]
            end_2 = secondList[j][1]

            if start_1 <= start_2:
                if end_1 >= start_2:    #overlap
                    S = max(start_1,start_2)
                    E = min(end_1,end_2)
                    result.append([S,E])
            else:                       #start_1 >= start_2
                if end_2 >= start_1:    #overlap
                    S = max(start_1,start_2)
                    E = min(end_1,end_2)
                    result.append([S,E])
            
            if end_1 <= end_2: #i wala khatam
                i += 1
            else:
                j += 1
        
        return result 