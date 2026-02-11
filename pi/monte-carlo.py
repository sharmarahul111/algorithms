# To estimate PI (π) using monte carlo
import random
import math

samples = 100000
radius = 1
in_circle = 0


def random_point():
    x = random.random()*2-1
    y = random.random()*2-1
    return x, y


# Using equation of circle
for i in range(samples):
    x, y = random_point()
    if x**2 + y**2 <= 1:
        in_circle += 1

# Using sin/cos
# for i in range(samples):
#     x,y = random_point()
#     x = abs(x)
#     y = abs(y)
#     angle = math.atan2(y,x)
#     rx = radius*math.cos(angle)
#     ry = radius*math.sin(angle)
#     if x<rx and y<ry:
#         in_circle = in_circle+1

pi = 4*in_circle/samples
print("Sample:", samples)
print("In circle:", in_circle)
print("Estimated value of π =", pi)
error = round(abs(math.pi-pi)/math.pi*100, 3)
print(f"Percentage error = {error}%")
