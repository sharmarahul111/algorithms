import matplotlib.pyplot as plt
from array import array
COUNT = 100000
x = array('i', range(1, COUNT+1))
y = array('i', [])

s = {1, 2, 4}


def nextTerm(n):
    return int(n/2) if n % 2 == 0 else 3*n+1


for i in x:
    max = i
    while i not in s:
        i = nextTerm(i)
        if i > max:
            max = i
    y.append(max)
    print(f"\r{len(y)/COUNT*100:.2f}%", flush=True, end="")
# print(y)
print()
plt.plot(y)
plt.title(f"First {COUNT} max collatz")
plt.xlabel("Number")
plt.ylabel("Peak value")
plt.savefig("collatz-max.png")
print(f"Saved {COUNT} points!")
