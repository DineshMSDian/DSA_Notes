def GCD(a, b):
    gcd = 1
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd

def GCD_EUCLIDEAN(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n1 = int(input("N1: "))
n2 = int(input("N2: "))
print(GCD(n1, n2))
print(GCD_EUCLIDEAN(n1,n2))
