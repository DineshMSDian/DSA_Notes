class Solution:
    def sumNaturalNos(self, n):
        if n > 0:
            self.sumNaturalNos(n-1)
            num = []
            num.append(n)
            print(sum(num), end=" ")

n = int(input())
sol = Solution()
sol.sumNaturalNos(n)