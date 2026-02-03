'''
https://practice.geeksforgeeks.org/problems/triangle-pattern-1662285911/1/?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=pattern_17
www.naukri.com/code360/problems/alpha-hill_6581921

Input: 4
Output:
   A
  ABA
 ABCBA
ABCDCBA
'''


def Pattern(n):
    for i in range(1, n + 1):
        alpha = 65
        for j in range(n - i):
            print(" ", end="")
        for k in range(2 * i - 1):  # 2*i-1 = 2(1)-1=1, 2(2)-1=3 ...5
            print(chr(alpha), end="")
            if i - 1 > k:  # i=1,2,3  , k=1,3,5
                alpha += 1
            else:
                alpha -= 1
        print()

n = int(input("Enter N value: "))
Pattern(n)