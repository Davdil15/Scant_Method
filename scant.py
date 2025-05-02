import numpy as np

def func(x):
    return np.exp(-x) - x

def secant(x0, x1, tol):
    i = 0
    while abs(func(x1)) > tol:
        if func(x1) - func(x0) == 0:
            print("There is division by zero.")
            return x1
        x_temp = x1 - (func(x1) * (x0 - x1)) / (func(x0) - func(x1))
        print('{:2d} {:7.4f} {:7.4f} {:7.4f} {:7.4f}'
      .format(i, x0, x1, x_temp, func(x1)), flush=True)
        x0 = x1
        x1 = x_temp
        i += 1
    return x1

# Pemanggilan func
x0 = 1
x1 = 0.6127
tol = 0.000001
print("results of the secant method: ")
print("i  x0       x1       x_temp   f(x1)")
result = secant(x0, x1, tol)
print("the root result is:", round(result, 4))
