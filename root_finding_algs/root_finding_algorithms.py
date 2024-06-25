import matplotlib.pyplot as plt

a = 0
b = 5


def f(x):
    return x ** 2 - x - 2


def phi(x, alpha):
    return alpha * f(x) + x


def bisect_step(a, b):
    return (a + b) / 2


def f_prime(x):
    return 2 * x - 1


def newton_step(x):
    return x - f(x) / f_prime(x)


def bisect_method(n, a, b, root):
    iterations = []
    steps_size = []
    errors = []
    current_approximation = []
    c = bisect_step(a, b)
    for i in range(0, n):
        if (f(a) * f(c) < 0):
            b = c
        elif (f(b) * f(c) < 0):
            a = c
        else:
            break
        steps_size.append(abs(c - (a + b) / 2))
        c = (a + b) / 2
        current_approximation.append(c)
        err = root - c
        iterations.append(i)
        errors.append(abs(err))
        # print(c, err)
    return iterations, current_approximation, steps_size, errors


def fixed_point_method(n, x0, root, alpha):
    iterations = []
    steps_size = []
    errors = []
    current_approximation = []
    for i in range(0, n):
        steps_size.append(abs(x0 - phi(x0, alpha)))
        x0 = phi(x0, alpha)
        current_approximation.append(x0)
        err = root - x0
        iterations.append(i)
        errors.append(abs(err))
        # print(x0, err)
    return iterations, current_approximation, steps_size, errors

def newton_method(n, x0, root):
    iterations = []
    steps_size = []
    errors = []
    current_approximation = []
    for i in range(0, n):
        steps_size.append(abs(x0 - newton_step(x0)))
        x0 = newton_step(x0)
        current_approximation.append(x0)
        err = root - x0
        iterations.append(i)
        errors.append(abs(err))
        # print(x0, err)
    return iterations, current_approximation, steps_size, errors


# Compute results
bisect_iterations, bisect_current_approximation, bisect_steps_size, bisect_errors = bisect_method(20, a, b, 2)
fixed_iterations, fixed_current_approximation, fixed_steps_size, fixed_errors = fixed_point_method(20, 3, 2, -0.2)
newton_iterations, newton_current_approximation, newton_steps_size, newton_errors = newton_method(20, 3, 2)

# Plotting
plt.figure(figsize=(18, 6))

# Function value at current approximation
plt.subplot(1, 3, 1)
plt.plot(bisect_iterations, [f(x) for x in bisect_current_approximation], label='Bisection Method')
plt.plot(fixed_iterations, [f(x) for x in fixed_current_approximation], label='Fixed Point Method')
plt.plot(newton_iterations, [f(x) for x in newton_current_approximation], label='Newton\'s Method')
plt.xlabel('Iteration number')
plt.ylabel('f(x_k)')
plt.title('Function value at current approximation')
plt.legend()

# Step size
plt.subplot(1, 3, 2)
plt.plot(bisect_iterations, bisect_steps_size, label='Bisection Method')
plt.plot(fixed_iterations, fixed_steps_size, label='Fixed Point Method')
plt.plot(newton_iterations, newton_steps_size, label='Newton\'s Method')
plt.xlabel('Iteration number')
plt.ylabel('Step size')
plt.title('Distance between x_k and x_{k+1}')
plt.legend()

# Distance between x_k and real solution
plt.subplot(1, 3, 3)
plt.plot(bisect_iterations, bisect_errors, label='Bisection Method')
plt.plot(fixed_iterations, fixed_errors, label='Fixed Point Method')
plt.plot(newton_iterations, newton_errors, label='Newton\'s Method')
plt.xlabel('Iteration number')
plt.ylabel('Error')
plt.title('Distance between x_k and real solution')
plt.legend()

plt.tight_layout()
plt.show()