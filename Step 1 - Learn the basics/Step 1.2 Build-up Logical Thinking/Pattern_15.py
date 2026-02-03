'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285196/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_15
https://www.naukri.com/code360/problems/reverse-letter-triangle_6581906

Input: 5

Output:
ABCDE
ABCD
ABC
AB
A
'''


def Pattern(n):
    for i in range(n, 0, -1):
        alpha = 65
        for j in range(i):
            print(chr(alpha), end="")
            alpha += 1
        print()

n = int(input("Enter N value: "))
Pattern(n)