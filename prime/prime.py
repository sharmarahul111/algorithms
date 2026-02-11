import matplotlib.pyplot as plt
from array import array
COUNT = 20000
x = array('i',range(1,COUNT+1))
y = array('i',[2])
# z = [1]
a = 3
while len(y) < COUNT:
    for i in y:
        if a%i==0:
            break
    else:
        y.append(a)
        # z.append(len(y))
    a+=2
    print(f"\r{len(y)/COUNT*100:.2f}%",flush=True,end="")
plt.plot(x,y)
# plt.plot(x,z,c="g")
plt.title(f"First {COUNT} primes")
plt.savefig("prime.png")
print("\nSaved!")
print(x,y)
