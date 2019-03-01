""" Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass? """

# Brute Force N**2
k = 20
nums = [2, 5, 8, 3, 17]

for i in nums:
    for j in nums[(i+1):]:
        if i == j:
            pass
        if i + j == k:
            print("True", i, j)

# List comprehension version
for i in nums:
    match = [i for x in nums[(i+1):] if i + x == k]
    if match:
        print(match, "True")

# Optimize
import itertools

for t in itertools.combinations(nums,2):
    if sum(t) == k:
        print([nums.index(a) for a in t])

# Using sets
seen = set()
for num in nums:
    if k - num in seen:
        print("True")
    else:
        seen.add(num)    