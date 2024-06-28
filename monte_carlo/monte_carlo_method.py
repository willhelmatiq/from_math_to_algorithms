

from matplotlib import pyplot as plt
from numpy import random


# count pi for n points
def compute_pi(n):
    inside_sector = []
    outside_sector = []
    for i in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y < 1:
            inside_sector.append([x,y])
        else:
            outside_sector.append([x,y])

    return 4 * len(inside_sector) / n, inside_sector, outside_sector




n = 1000000  # Number of points
pi_estimate, inside_points, outside_points = compute_pi(n)

# Print the estimated value of pi
print(f"Estimated value of pi: {pi_estimate}")

# Separate the x and y coordinates for plotting
inside_x, inside_y = zip(*inside_points)
outside_x, outside_y = zip(*outside_points)

# Plotting the points
plt.figure(figsize=(5, 5))
plt.scatter(inside_x, inside_y, color='red', label='Inside Sector')
plt.scatter(outside_x, outside_y, color='blue', label='Outside Sector')
# plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title(f"Monte-Carlo Estimation of Pi with {n} Points")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()