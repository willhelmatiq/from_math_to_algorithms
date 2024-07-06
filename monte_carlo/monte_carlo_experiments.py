import math
import random

import numpy as np
from matplotlib import pyplot as plt


def compute_pi(n):
    inside_sector = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y < 1:
            inside_sector += 1
    return 4 * inside_sector / n


def compute_pi_with_error(n_start, n_end, step):
    error = []
    number_of_points = []
    for i in range(n_start, n_end + 1, step):
        error.append(abs(math.pi - compute_pi(i)))
        number_of_points.append(i)
    return error, number_of_points

def compute_pi_with_error_average(n_start, n_end, step, n):
    error = []
    number_of_points = []
    for j in range(n):
        for i in range(n_start, n_end + 1, step):
            if j == 0:
                error.append(abs(math.pi - compute_pi(i)))
                number_of_points.append(i)
            else:
                error[int((i - n_start)/ step)] += abs(math.pi - compute_pi(i))

    for j in range(len(error)):
        error[j] = error[j] / n
    return error, number_of_points

n_start = 1000
n_end = 100000
step = 1000

# Compute errors and number of points
# errors, number_of_points = compute_pi_with_error(n_start, n_end, step)
errors_average, number_of_points_average = compute_pi_with_error_average(n_start, n_end, step, 100)

# Plotting the results
plt.figure(figsize=(10, 6))

# plt.plot(number_of_points, errors, marker='o', linestyle='-', color='b')
# plt.xscale('log')  # Use logarithmic scale for x-axis
# plt.yscale('log')  # Use logarithmic scale for y-axis
# plt.title('Error in Estimating π using Monte Carlo Simulation')
# plt.xlabel('Number of Points')
# plt.ylabel('Error (|π - Estimated π|)')
# plt.grid(True)
# plt.tight_layout()


plt.plot(number_of_points_average, errors_average, marker='o', linestyle='-', color='r')
plt.xscale('log')  # Use logarithmic scale for x-axis
plt.yscale('log')  # Use logarithmic scale for y-axis
plt.title('Error in Estimating π using Monte Carlo Simulation')
plt.xlabel('Number of Points')
plt.ylabel('Error (|π - Estimated π|)')
plt.grid(True)
plt.tight_layout()

plt.show()

