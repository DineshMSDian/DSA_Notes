# Brute Force approach TC O(nlogn)

"""
def isAnagram(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    if ''.join(sorted_s) == ''.join(sorted_t):
        return True
    else:
        return False
"""


# Optimal Approach
from collections import Counter
# Counter()
"""
num = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(Counter(nums))

Output:
Counter({4: 4, 3: 3, 2: 2, 1: 1})

Explanation: Counter object shows that 4 appears 4 times, 3 appears 3 times, 2 appears 2 times and 1 appears once.
"""
def isAnagram(s, t):
        return Counter(s) == Counter(t)

s = "anagram"
t = "nagaram"

print(isAnagram(s, t))