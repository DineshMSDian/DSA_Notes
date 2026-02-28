class Solution:

    def printGFG(self,n):

        if n == 0:
            return

        print("GFG", end=" ")
        self.printGFG(n-1)

n = int(input())
sol = Solution()
sol.printGFG(n)