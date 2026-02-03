# https://practice.geeksforgeeks.org/problems/right-triangle/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_2

"""
n=3
*
**
***
"""
def Pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end="")
        print()

n = int(input("Enter N value: "))
Pattern(n)