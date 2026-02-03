# https://www.geeksforgeeks.org/problems/reverse-digit0316/
# https://www.naukri.com/code360/problems/reverse-of-a-number_624652?leftPanelTabValue=PROBLEM

def ReverseNumber(n):
    revNum = 0

    while n > 0:
        last_digit = n % 10
        revNum = (revNum * 10) + last_digit
        n = n // 10
    return revNum

n = int(input("Enter N value: "))
print(ReverseNumber(n))