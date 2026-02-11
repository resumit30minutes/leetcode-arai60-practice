class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_first_appear_index = {}
        duplicated = set()
        for index, c in enumerate(s):
            if c in duplicated:
                continue
            if c in char_to_first_appear_index:
                del char_to_first_appear_index[c]
                duplicated.add(c)
                continue
            char_to_first_appear_index[c] = index
        if not char_to_first_appear_index:
            return -1
        return next(iter(char_to_first_appear_index.values()))
            
