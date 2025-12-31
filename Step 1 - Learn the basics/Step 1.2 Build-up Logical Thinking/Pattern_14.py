'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1662284916/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_14
https://www.naukri.com/code360/problems/increasing-letter-triangle_6581897

Input: 5

Output:
A
AB
ABC
ABCD
ABCDE

'''


def Pattern(n):
    for i in range(1, n + 1):
        alpha = 65
        for j in range(1, i + 1):
            print(chr(alpha), end="")
            alpha += 1
        print()

n = int(input("Enter N value: "))
Pattern(n)