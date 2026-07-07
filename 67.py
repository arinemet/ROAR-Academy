import time
import math


def ncr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


tic = time.time()
n = 800
for i in range(0, n + 1):
    for j in range(0, i + 1):
        print(math.comb(i, j), end=" ")
    print()
toc = time.time()
print(f"Time taken: {toc - tic:0.10f} seconds")
