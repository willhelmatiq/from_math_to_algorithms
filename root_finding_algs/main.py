import matplotlib.pyplot as plt

a = 0
b = 5

def f(x):
    return x ** 2 - x - 2

def phi(x, alpha):
    return alpha * f(x) + x

def bisect_step(a, b):
    return (a + b) / 2

def bisect_method(n, a, b, root):
    c = bisect_step(a, b)
    iterations = []
    errors = []
    for i in range(0, n):
        if (f(a) * f(c) < 0):
            b = c
        elif(f(b) * f(c) < 0):
            a = c
        else:
            break
        c = (a + b) / 2
        err = root - c
        iterations.append(i)
        errors.append(abs(err))
        print(c, err)
    return iterations, errors

def fixed_point_method(n, x0, root):
    iterations = []
    errors = []
    for i in range(0, n):
        x0 = phi(x0, -0.2)
        err = root - x0
        iterations.append(i)
        errors.append(abs(err))
        print(x0, err)
    return iterations, errors

# Compute results
bisect_iterations, bisect_errors = bisect_method(20, a, b, 2)
fixed_iterations, fixed_errors = fixed_point_method(20, 3, 2)

# Plot results
plt.figure(figsize=(10, 5))

plt.plot(bisect_iterations, bisect_errors, label='Bisection Method', marker='o', color='blue')
plt.plot(fixed_iterations, fixed_errors, label='Fixed-Point Method', marker='o', color='orange')

plt.xlabel('Iteration')
plt.ylabel('Error')
plt.title('Convergence of Bisection and Fixed-Point Methods')
plt.legend()
plt.grid(True)

plt.show()
