'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718712/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_13
https://www.naukri.com/code360/problems/increasing-number-triangle_6581893

Input: 5

Output:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''


def Pattern(n):
    num = 1
    for i in range(num, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

n = int(input("Enter N value: "))
Pattern(n)
