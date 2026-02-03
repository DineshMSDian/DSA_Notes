# https://leetcode.com/problems/palindrome-number

def isPalindrome(n):
    temp = n
    revNum = 0

    while temp > 0:
        last_digit = temp % 10
        temp = temp // 10
        revNum = (revNum * 10) + last_digit

    if revNum == n:
        return True
    else:
        return False

n = int(input("Enter N value: "))
print(isPalindrome(n))

