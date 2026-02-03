# Prob link 1: https://practice.geeksforgeeks.org/problems/count-digits5716/1
# prob link 2: https://www.naukri.com/code360/problems/number-of-digits_9173
'''
 Problem statement

You are given a number 'n'.

Return number of digits in ‘n’.

Example:

Input: 'n' = 123

Output: 3

Explanation:
The 3 digits in ‘123’ are 1, 2 and 3. 

'''
from itertools import count


def CountDigits(n):
    Count = []
    while n > 0:
        last_digit = n % 10
        n = n // 10
        Count.append(last_digit)

    print(len(Count))


n = int(input("Enter N value: "))
CountDigits(n)

"""
Input:
N = 12
Output:
2
Explanation:
1, 2 both divide 12 evenly

Input:
N = 23
Output
0
Explanation:
2 and 3, none of them
divide 23 evenly
"""

def evenlyDivides(n):
    count = 0
    temp = n

    while n > 0:
        last_digit = n % 10
        n = n // 10
        if last_digit != 0:
            if temp % last_digit == 0:
                count += 1

    print(count)




n = int(input("Enter N value: "))
evenlyDivides(n)
