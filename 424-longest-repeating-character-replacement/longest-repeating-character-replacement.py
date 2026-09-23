class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        longest = 0
        max_freq_number = 0

        for right in range(len(s)):

            
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq_number = max(max_freq_number, freq[s[right]])

            
            while (right - left + 1) - max_freq_number > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            # Valid window
            longest = max(longest, right - left + 1)

        return longest