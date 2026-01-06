# https://www.geeksforgeeks.org/problems/prime-number2314/1
# https://www.naukri.com/code360/problems/check-prime_624934?leftPanelTabValue=PROBLEM

import math

def isPrime(n):

    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1

    if count == 2:
        return True
    else:
        return False

n = int(input("Enter N value: "))
i = int(input("Enter i value"))
print(n % i == 0)
print(i != n // i)
print(isPrime(n))


