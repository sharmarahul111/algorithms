import numpy as np
# primes upto n
n = 5000000
# 1 denotes prime
# 0 denotes non prime
lst = np.ones((n,), dtype=int)
lst[0] = lst[1] = 0
# current prime (divider)
for i in range(n):
    if lst[i] == 0:
        continue
    for j in range(i+i, n, i):
        lst[j] = 0

# display the primes
# print(lst)
# for i in range(n):
#     if lst[i]:
#         print(i, end=",")
print()
print(f"Number of primes:{lst.sum()}")
