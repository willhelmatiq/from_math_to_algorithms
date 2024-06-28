import math
import random


def compute_n_and_pi(eps):
    inside_sector = 0
    i = 0
    pi_from_monte_carlo = 1
    while abs(math.pi - pi_from_monte_carlo) > eps:
        x = random.random()
        y = random.random()
        if x * x + y * y < 1:
            inside_sector += 1
        pi_from_monte_carlo = 4 * inside_sector / (i + 1)
        i += 1
    return pi_from_monte_carlo, i + 1

eps = 0.00001

pi_from_monte_carlo, number_of_points = compute_n_and_pi(eps)

print(f"pi_from_monte_carlo: {pi_from_monte_carlo} number of iteration: {number_of_points}")

def average_compute_n_and_pi(eps, n):
    pi_from_monte_carlo = 0
    number_of_points = 0
    for i in range(n):
        pi_temp, number_temp = compute_n_and_pi(eps)
        # print(number_temp)
        pi_from_monte_carlo += pi_temp
        number_of_points += number_temp
    # print(number_of_points)
    return pi_from_monte_carlo / n, number_of_points / n

pi_from_monte_carlo_average, number_of_points_average = average_compute_n_and_pi(eps, 100)

print(f"pi_from_monte_carlo_average: {pi_from_monte_carlo_average} average number of iteration: {number_of_points_average}")