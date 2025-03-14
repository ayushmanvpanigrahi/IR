def editDistance(Str1, Str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if Str1[m - 1] == Str2[n - 1]:
        return editDistance(Str1, Str2, m - 1, n - 1)
    return 1 + min(editDistance(Str1, Str2, m, n - 1), 
                   editDistance(Str1, Str2, m - 1, n), 
                   editDistance(Str1, Str2, m - 1, n - 1))

Str1 = "Sunday"
Str2 = "Saturday"
print(editDistance(Str1, Str2, len(Str1), len(Str2)))