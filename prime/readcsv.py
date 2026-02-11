import numpy as np
import matplotlib.pyplot as plt
print("Reading file...",end="")
with open("data.csv") as f:
    data = np.fromstring(f.read(), dtype=int, sep=",")
print("\rFile read...")
plt.plot(data)
plt.savefig("cprime.png")
print("File saved!");
