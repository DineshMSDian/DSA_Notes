'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285334/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_16
https://www.naukri.com/code360/problems/alpha-ramp_6581888

Input: 5

Output:
A
BB
CCC
DDDD
EEEEE

'''


def Pattern(n):
    alpha = 65
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(alpha), end="")
        alpha += 1
        print()

n = int(input("Enter N value: "))
Pattern(n)