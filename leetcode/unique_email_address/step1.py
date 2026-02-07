from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def normalize(before):
            normalized = []
            i = 0
            while i < len(before):
                char = before[i]
                if char == '@':
                    while i < len(before):
                        normalized.append(before[i])
                        i += 1
                    break

                if char == '.':
                    i += 1
                    continue
                
                if char == '+':
                    while i < len(before) and before[i] != '@':
                        i += 1
                    continue
                
                normalized.append(char)
                i += 1
            return "".join(normalized)
                
        
        normalized_emails = set()
        for email in emails:
            normalized_emails.add(normalize(email))

        return len(normalized_emails)
