import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective_function(x):
    # Example objective function: Rosenbrock function
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

# Define the first derivative of the objective function
def gradient(x):
    dfdx0 = -2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0]**2)
    dfdx1 = 200 * (x[1] - x[0]**2)
    return np.array([dfdx0, dfdx1])

# Define the second derivative of the objective function (Hessian matrix)
def hessian(x):
    d2fdx02 = 2 - 400 * (x[1] - 3 * x[0]**2)
    d2fdx0dx1 = -400 * x[0]
    d2fdx12 = 200
    return np.array([[d2fdx02, d2fdx0dx1],
                     [d2fdx0dx1, d2fdx12]])

# Initial guess
initial_guess = np.array([0, 0])

# Define bounds (if any)
bounds = ((-5, 5), (-5, 5))  # Bounds for each variable (x1, x2)

# Perform optimization
result = minimize(objective_function, initial_guess, method='trust-constr', jac=gradient, hess=hessian, bounds=bounds)

# Print results
print("Optimal solution:")
print("x1 =", result.x[0])
print("x2 =", result.x[1])
print("Objective value =", result.fun)
