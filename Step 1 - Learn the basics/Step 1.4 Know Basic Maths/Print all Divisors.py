# https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1
# https://www.naukri.com/code360/problems/print-all-divisors-of-a-number_1164188?leftPanelTabValue=PROBLEM
import math

def print_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) +1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()

    for div in divisors:
        print(div, end=" ")

n = int(input("Enter N value: "))
print(print_divisors(n))