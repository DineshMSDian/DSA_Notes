def isAnagram(s, t):
    d = {}
    if len(s) != len(t):
        return False
    
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    for j in t:
        if j not in d:
            return False
        else:
            if d[j] == 1:
                del d[j]
            else:
                d[j] -= 1
    return not d
    
s = 'anagram'
t = 'nagaram'
print(isAnagram(s, t))