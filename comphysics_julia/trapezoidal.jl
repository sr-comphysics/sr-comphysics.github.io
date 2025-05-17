################################################################################
# Title:         Trapezoidal Rule Integration in Julia
# Description:   This program approximates the definite integral of a given
#                function f(x) over the interval [a, b] using the trapezoidal
#                rule. The function 'trapezoidal' computes and returns the
#                approximated value given the number of subintervals n.
#
# Instructions:
#   1. Save this file as, for example, trapezoidal.jl.
#   2. To run the program, open a terminal and navigate to the file's directory.
#   3. Execute the program with the command: julia trapezoidal.jl
################################################################################

# The trapezoidal rule to approximate the definite integral of function f
#          over the interval [a, b] using n subdivisions.
function trapezoidal(a, b, n, f)
    # Calculate the width of each subinterval.
    h = (b - a) / n

    # Initialize sum 's' with the average of the function values at the endpoints.
    s = (f(a) + f(b)) / 2

    # Loop over each interior point (i=1 to n-1) and accumulate the function values.
    for i in 1:(n - 1)
        s += f(a + i * h)  # Evaluate f at the current x value and add to the sum.
    end

    # Multiply the accumulated sum with the width 'h' to get the final approximation.
    y = h * s

    # Return the approximated integral value.
    return y
end

# Define the function 'f(x)' as an anonymous function.
# In this example, f(x) = x^2 * sin(x),
f = x -> x^2 * sin(x);

# If you wish to test a different function, simply modify the definition above.
# For example, you can try:
# f = t -> t^2 + 1 or anything

# Compute the approximate integral of f over the interval [0, 1] using 4 subintervals.
y = trapezoidal(0, 1, 4, f)

# Print the result to the console.
println("Trapezoidal; y= ", y)
