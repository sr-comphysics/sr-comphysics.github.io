# Solving a Linear Equation Using SymPy
# Importing necessary functions from the sympy library
from sympy import symbols, Eq, solve  # Importing symbols for variable definition, Eq for equation creation, and solve for solving equations

# Define the variable
x = symbols('x')  # Creating a symbolic variable x

# Define the linear equation
eq = Eq(2*x + 3, 9)  # Defining the equation 2x + 3 = 9 using the Eq function

# Solve the equation
sol = solve(eq, x)  # Solving the equation for the variable x

# Printing the solution
print("Solution:", sol)  # Displaying the solution to the equation
