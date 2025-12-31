'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1661718455/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_11
https://www.naukri.com/code360/problems/binary-number-triangle_6581890?leftPanelTabValue=PROBLEM
Input: 5

Output:
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

'''


def Pattern(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            num = 0
        else:
            num = 1
        for j in range(i):
            print(num, end="")
            num = 1 - num
        print()

n = int(input("Enter N value: "))
Pattern(n)
