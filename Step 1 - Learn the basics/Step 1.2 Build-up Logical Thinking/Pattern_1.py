# https://practice.geeksforgeeks.org/problems/square-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_1

"""
n = 4
*****
*****
*****
*****
"""


def Pattern(n):
    for i in range(1, n + 1):
        for j in range(n):
            print("*", end="")
        print()

n = int(input("Enter N value: "))
Pattern(n)