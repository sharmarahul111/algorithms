import numpy as np
import matplotlib.pyplot as plt
print("Reading file...", end="")
with open("data.csv") as f:
    data = np.fromstring(f.read(), dtype=int, sep=",")
print("\rFile read...")
# plt.plot(np.diff(data[:1000]))
i = np.arange(1, len(data)+1)
# i = np.log(i)
# plt.plot(data/i)

d = np.diff(data)
plt.hist(d, bins=range(0, int(max(d)+1)),)
plt.title("Consecutive difference of primes")
plt.ylabel("Primes")
plt.xlabel("Difference")
plt.savefig("diff-cprime.png")
print("File saved!")
