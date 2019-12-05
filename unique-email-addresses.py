class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            domain = email[email.find('@'):]
            name = email[:email.find('@')]
            if '+' in name: name = name[:name.find('+')]
            name = name.replace('.','')
            unique.add(name+domain)
        return len(unique)
#### O(n*m); 98, 100 Python3