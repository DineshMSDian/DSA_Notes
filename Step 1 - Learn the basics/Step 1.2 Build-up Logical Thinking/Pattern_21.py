'''
https://practice.geeksforgeeks.org/problems/square-pattern-1662287714/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_21
https://www.naukri.com/code360/problems/ninja-and-the-star-pattern-i_6581920

Input: 4
Output:
****
*  *
*  *
****
'''


def Pattern(n):
    print("*" * n)
    for i in range(n - 2):
        for j in range(1):
            print("*", end="")
        for k in range(n - 2):
            print(" ", end="")
        for l in range(1):
            print("*", end="")
        print()
    print("*" * n)

n = int(input("Enter N value: "))
Pattern(n)