class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):

            if s[i] in "({[":
                stack.append(s[i])

            else:
                if not stack:  # without opening bracket # Khali honi chahiye , non-Empty hai abhi 
                    return False

                if s[i] == ")" and stack[-1] != "(":
                    return False

                if s[i] == "}" and stack[-1] != "{":
                    return False

                if s[i] == "]" and stack[-1] != "[":
                    return False

                stack.pop()

        return len(stack) == 0  #kya sare brackets band ho gye?