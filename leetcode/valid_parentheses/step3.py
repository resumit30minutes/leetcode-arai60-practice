
class Solution:
    def isValid(self, s: str) -> bool:
        open_to_closed_brackets = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        expected_closed_brackets = []
        for c in s:
            if c in open_to_closed_brackets:
                expected_closed_brackets.append(open_to_closed_brackets[c])
                continue

            if expected_closed_brackets == []:
                return False

            if expected_closed_brackets[-1] != c:
                return False
            expected_closed_brackets.pop()

        return expected_closed_brackets == []
