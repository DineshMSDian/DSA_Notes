'''
https://practice.geeksforgeeks.org/problems/double-triangle-pattern/1/?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_19
https://www.naukri.com/code360/problems/symmetric-void_6581919

Input: 5
Output:
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''


def Pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        for k in range(n - i):
            print(" ", end=" ")
        for l in range(i):
            print("*", end="")
        print()

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        for k in range(n - i):
            print(" ", end=" ")
        for l in range(i):
            print("*", end="")
        print()

n = int(input("Enter N value: "))
Pattern(n)