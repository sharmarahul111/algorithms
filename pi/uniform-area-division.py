# Calculate pi (π) by uniformly distributed
# points in a square where a circle is inscribed

import math

divisions = 5000
radius = 1
in_circle = 0


# Using equation of circle
for i in range(divisions):
    # show a progress bar
    # if((i+1)%50==0):
    print(f"\r{((i+1)/divisions*100):0.2f}%", end="", flush=True)
    for j in range(divisions):
        x = i/divisions
        y = j/divisions
        if x**2 + y**2 <= 1:
            in_circle += 1

print()
pi = 4*in_circle/(divisions**2)
print("Total points:", divisions**2)
print("In circle:", in_circle)
print("Estimated value of π =", pi)
error = round(abs(math.pi-pi)/math.pi*100, 3)
print(f"Percentage error = {error}%")
