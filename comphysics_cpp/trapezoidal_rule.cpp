/*
 * Title: Numerical Integration Using the Trapezoidal Rule
 *
 * Description:
 * This program approximates the definite integral of a function using
 * the trapezoidal rule. The function f(x) is defined as:
 *
 *      f(x) = x^2 + 0.1
 *
 * The user is prompted to enter the endpoints a and b of the integration interval,
 * along with the number of subintervals (n) to use in the approximation. The trapezoidal
 * rule formula is applied:
 *
 *      Integral ≈ h * [(f(a) + f(b)) / 2 + sum(f(x_i) for i=1 to n-1)]
 *
 * where h = (b - a) / n and x_i are the internal points of the partition.
 *
 * Compiler Note:
 * Compile this program using g++:
 *      g++ -o trapezoidal_rule trapezoidal_rule.cpp -lm
 * The "-lm" flag links the math library for functions such as pow().
 */

#include <iostream>   // Provides input/output functionality (cin, cout)
#include <cmath>      // Provides the pow() function and other math functions

using namespace std;  // Allows usage of standard library entities without the "std::" prefix

// Function prototype for f(x)
double f(double x);

int main()
{
    // Inform the user that the trapezoidal rule method is being used.
    cout << "Trapezoidal rule: \n";

    // Declare variables for the number of subintervals (n) and the endpoints of the interval.
    int n;
    double a, b;

    // Declare variables for the step size (h), the current x value, function value (y),
    // and the sum (s) used for the numerical integration.
    double h, x, y, s;

    // Prompt the user to input the endpoints of the interval [a, b].
    cout << "Enter interval endpoints (a, b): \n";
    cin >> a >> b;

    // Prompt the user to input the number of subintervals (n) to use for the approximation.
    cout << "Enter the number of subintervals (n): ";
    cin >> n;

    // Calculate the step size (h) based on the interval length and the number of subintervals.
    h = (b - a) / n;

    // Initialize the summation variable (s) to zero.
    s = 0;
    x = a;

    // Loop to sum the function evaluations at internal points of the interval.
    // The endpoints f(a) and f(b) are handled separately.
    for (int i = 1; i <= n - 1; i++)
    {
        x += h;         // Increment the x value by the step size.
        y = f(x);       // Evaluate the function at the current x.
        s += y;         // Accumulate the sum of function values.
    }

    // Apply the trapezoidal rule:
    // Integral ≈ h * [(f(a) + f(b)) / 2 + s]
    s = h * ((f(a) + f(b)) / 2 + s);

    // Output the approximate value of the integral.
    cout << "Approximate value using " << n << " subintervals: " << s << endl;

    return 0;  // Successful termination of the program.
}

// Function definition for f(x)
// Returns the value of the function f(x) = x^2 + 0.1
double f(double x)
{
    return pow(x, 2) + 0.1;
}
