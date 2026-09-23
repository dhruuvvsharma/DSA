class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0 
        right = 0 
        freq = {}
        maximum_fruits = 0

        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right],0) + 1

            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]

                left += 1
            
            maximum_fruits = max(maximum_fruits,right - left + 1)
        
        return maximum_fruits