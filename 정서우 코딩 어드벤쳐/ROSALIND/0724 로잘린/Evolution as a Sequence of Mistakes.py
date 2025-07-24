# Evolution as a Sequence of Mistakes

# Problem

# Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
# Given two strings s
#  and t
#  of equal length, the Hamming distance between s
#  and t
# , denoted dH(s,t)
# , is the number of corresponding symbols that differ in s
#  and t
# . See Figure 2.

# Given: Two DNA strings s
#  and t
#  of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t)
# .

# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# Sample Output
# 7

s = list(str(input()))
t = list(str(input()))

hamming_distance = 0
for i in range(len(s)):
    if s[i] != t[i]:
        hamming_distance += 1

print(hamming_distance)


