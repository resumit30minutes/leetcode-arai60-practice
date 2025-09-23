class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_closed_bracket_dict = {
            '(': ')',
            '{': '}',
            '[': ']',  
        }

        for bracket in s:
            if bracket in open_to_closed_bracket_dict:
                stack.append(bracket)
                continue

            if stack == []:
                return False
            
            expected = open_to_closed_bracket_dict[stack.pop()]
            if bracket != expected:
                return False
            
        return True if not stack else False