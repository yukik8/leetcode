class Solution:
    def numUniqueEmails(self, emails):
        answer = set()
        for address in emails:
            local,domain = address.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            answer.add(local+domain)
        print(answer)
        print(len(answer))
        return len(answer)