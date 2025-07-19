# Conditions and Loops

# Problem
# Given: Two positive integers aand b
#  (a<b<10000).

# Return: The sum of all odd integers from a through b, inclusively.

# Sample Dataset
# 100 200
# Sample Output
# 7500

a, b = map(int, input().split())

num_list = []

for i in range(a, b + 1):
    if i % 2 == 0:
        pass
    elif i % 2 == 1:
        num_list.append(i)

print(sum(num_list))
