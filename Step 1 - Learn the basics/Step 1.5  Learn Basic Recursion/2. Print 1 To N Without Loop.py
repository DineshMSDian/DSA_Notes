class Solution:
    def Printnos(self, n):

        if n > 0:
            self.Printnos(n-1)
            print(n, end=" ")

n = int(input())
sol = Solution()
sol.Printnos(n)
