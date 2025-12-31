'''

https://practice.geeksforgeeks.org/problems/pattern/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_9


    *
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''


def Pattern(n):
    for i in range(1, n + 1):  # Space should decrease 2 -> 1 -> 0
        for j in range(n - i):  # n = 3, i = 1, n = 3, i = 2, n = 3, i = 1
            print(" ", end="")  #
        for k in range(2 * i - 1):
            print("*", end="")
        print()

    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()

n = int(input("Enter N value: "))
Pattern(n)
