class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            match char:
                case '(':
                    stack.append(')')
                case '{':
                    stack.append('}')
                case '[':
                    stack.append(']')
                case _:
                    expected = stack.pop() if stack else ''
                    if char != expected:
                        return False
        
        return True if not stack else False