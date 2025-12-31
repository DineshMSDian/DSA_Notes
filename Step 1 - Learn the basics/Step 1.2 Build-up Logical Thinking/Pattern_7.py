# https://practice.geeksforgeeks.org/problems/triangle-pattern-1661492263/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_7

# Input: 5

# Output:
'''
    *
   ***
  *****
 *******
*********
'''


def Pattern(n):  # itr_1 n = 3, i = 1, itr_2 n = 3, i = 2
    for i in range(1, n + 1):  # n - i = 3 - 1 = 2 space , n - i = 3 - 2 = 1 space
        for j in range(n - i):  # Space should decrease in n -1 ie 2 -> 1 -> 0
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()

n = int(input("Enter N value: "))
Pattern(n)