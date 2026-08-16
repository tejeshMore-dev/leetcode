class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)
        email_to_account = defaultdict(list)

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_to_account[email].append(i)
        
        for account_indexes in email_to_account.values():
            if len(account_indexes) > 1:
                for i in range(1, len(account_indexes)):
                    dsu.union(account_indexes[0], account_indexes[i])

        account_index_to_emails = defaultdict(set)
        for i, account in enumerate(accounts):
            parent = dsu.find(i)

            for j in range(1, len(account)):
                email = account[j]
                account_index_to_emails[parent].add(email)
        
        ans = []
        for i, emails in account_index_to_emails.items():
            name = accounts[i][0]
            ans.append([ name ]  + sorted(list(emails)) )
        
        return ans