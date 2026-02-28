class Solution:
    def PrintNos(self, n):

        if n == 0:
            return

        print(n, end=" ")

        self.PrintNos(n-1)

n = int(input())
sol = Solution()
sol.PrintNos(n)