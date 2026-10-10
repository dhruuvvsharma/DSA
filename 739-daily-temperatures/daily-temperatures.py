class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0]*len(temperatures)
        
        result[len(temperatures)-1] = 0 #last index 
        stack.append(len(temperatures)-1)  #push last index, not element 

        for i in range(len(temperatures)-2,-1,-1):
            while stack and temperatures[stack[-1]] <=  temperatures[i]:
                stack.pop()
            if stack: #not empty 
                result[i] = stack[-1] - i 
            else:
                result[i] = 0
            
            stack.append(i)
        
        return result 
