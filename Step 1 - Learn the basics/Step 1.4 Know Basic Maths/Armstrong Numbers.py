# https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
# https://www.naukri.com/code360/problems/armstrong-number_1462443?leftPanelTabValue=PROBLEM

def ArmstrongNumbers(n):
    temp = n
    sum = 0

    while temp > 0:
        last_digit = temp % 10
        temp = temp // 10
        sum = sum + last_digit ** 3

    if sum == n:
        return True
    else:
        return False

n = int(input("Enter N value: "))
print(ArmstrongNumbers(n))
