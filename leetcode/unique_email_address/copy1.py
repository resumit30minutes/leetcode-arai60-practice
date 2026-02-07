from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def canonicalize_email(before):
            after = []
            local, domain = before.split("@")
            for c in local:
                if c == "+":
                    break
                if c == ".":
                    continue
                after.append(c)
            after.append("@")
            after.append(domain)
            return "".join(after)

        unique_emails = set()
        for email in emails:
            unique_emails.add(canonicalize_email(email))
        return len(unique_emails)
