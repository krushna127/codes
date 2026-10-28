# Practical 4: Gradient Descent Algorithm
# Find the local minimum of y = (x + 3)^2 starting from x = 2

import numpy as np
import matplotlib.pyplot as plt

# 1. Define function and derivative
def f(x):
    return (x + 3) ** 2

def grad_f(x):
    return 2 * (x + 3)

# 2. Initialize parameters
x_current = 2.0
learning_rate = 0.1
tolerance = 1e-6
max_iterations = 25
history = [x_current]

# 3. Gradient descent loop
for i in range(max_iterations):
    gradient = grad_f(x_current)
    x_next = x_current - learning_rate * gradient

    if abs(x_next - x_current) < tolerance:
        x_current = x_next
        history.append(x_current)
        print(f"Converged after {i + 1} iterations.")
        break

    x_current = x_next
    history.append(x_current)
    print(f"Iteration {i + 1}: x = {x_current:.4f}, f(x) = {f(x_current):.4f}")

# 4. Print result
print("Local minimum at x =", x_current)
print("Function value at local minimum y =", f(x_current))

# 5. Plot convergence
x_values = np.linspace(-4, 3, 200)
plt.plot(x_values, f(x_values), label="f(x) = (x + 3)^2")
plt.plot(history, [f(x) for x in history], marker="o", label="Gradient descent steps")
plt.xlabel("x values")
plt.ylabel("f(x)")
plt.title("Gradient Descent Convergence")
plt.grid(True)
plt.legend()
plt.show()
