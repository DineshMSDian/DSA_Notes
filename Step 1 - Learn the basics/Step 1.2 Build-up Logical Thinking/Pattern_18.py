'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1662286302/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_18
https://www.naukri.com/code360/problems/alpha-triangle_6581429

Input: 5

Output:
E
E D
E D C
E D C B
E D C B A
'''


def Pattern(n):
    for i in range(1, n + 1):
        alpha = 65 + n - i
        for j in range(i):
            print(chr(alpha), end="")
            alpha += 1
        print()

n = int(input("Enter N value: "))
Pattern(n)