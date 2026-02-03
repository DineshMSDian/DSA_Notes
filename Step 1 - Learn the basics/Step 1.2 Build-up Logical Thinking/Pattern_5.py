# https://practice.geeksforgeeks.org/problems/triangle-pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_5

# Input: 5

# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

def Pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print()

n = int(input("Enter N value: "))
Pattern(n)