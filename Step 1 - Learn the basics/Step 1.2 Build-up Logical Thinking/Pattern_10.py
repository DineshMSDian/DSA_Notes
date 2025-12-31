'''

https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718013/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_10

Input: 5

Output:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''


def Pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()

    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("*", end="")
        print()

n = int(input("Enter N value: "))
Pattern(n)
