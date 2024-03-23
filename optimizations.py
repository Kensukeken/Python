import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective_function(x):
    # Example objective function: Rosenbrock function
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

# Define constraints
def constraint_eq(x):
    return 2*x[0] + x[1] - 3

def constraint_ineq(x):
    return x[0] - x[1]

# Initial guess
initial_guess = np.array([0, 0])

# Define bounds (if any)
bounds = ((-5, 5), (-5, 5))  # Bounds for each variable (x1, x2)

# Define constraints
constraints = ({'type': 'eq', 'fun': constraint_eq},
               {'type': 'ineq', 'fun': constraint_ineq})

# Perform optimization
result = minimize(objective_function, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

# Print results
print("Optimal solution:")
print("x1 =", result.x[0])
print("x2 =", result.x[1])
print("Objective value =", result.fun)
