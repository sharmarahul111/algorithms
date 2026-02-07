# Calculate pi (π) by uniformly distributed
# points in a square where a circle is inscribed

import math

divisions = 2000
radius = 1
in_circle = 0

def random_point():
    x = random.random()*2-1
    y = random.random()*2-1
    return x,y

# Using equation of circle
for i in range(divisions):
    for j in range(divisions):
        x = i/divisions
        y = j/divisions
        if x**2 + y**2 <= 1:
            in_circle = in_circle+1


pi = 4*in_circle/(divisions**2)
print("Total points:", divisions**2)
print("In circle:", in_circle)
print("Estimated value of π =", pi)
error = round(abs(math.pi-pi)/math.pi*100,3)
print(f"Percentage error = {error}%")
