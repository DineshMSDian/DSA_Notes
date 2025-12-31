'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1661493231/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_8

Input: 5

Output:

*********
 *******
  *****
   ***
    *
'''


def Pattern(n):
    for i in range(n, 0, -1):  # space should increase 0 -> 1 -> 2
        for j in range(n - i):  # itr_1 n = 3,i = 3, itr_2 , n = 3, i = 2, itr_3 n = 3, i = 1
            print(" ", end="")  # n - i = 3 - 3 = 0 Spc, n - i = 3 - 2 = 1 Spc,   n - i = 3 - 1 = 2 Spc
        for k in range(2 * i - 1):
            print("*", end="")
        print()

n = int(input("Enter N value: "))
Pattern(n)