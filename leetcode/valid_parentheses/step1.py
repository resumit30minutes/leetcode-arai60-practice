
class Solution:
    def isValid(self, s: str) -> bool:
        valid_open_to_closed_bracket_map = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        expected_closed_brackets = []

        for char in s:
            if s in valid_open_to_closed_bracket_map:
                expected_closed_brackets.append(valid_open_to_closed_bracket_map[char])
                continue

            if expected_closed_brackets == []:
                return False


            if expected_closed_brackets.pop() != char:
                return False

        return expected_closed_brackets == []



