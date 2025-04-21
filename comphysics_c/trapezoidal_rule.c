/* Program Title: Numerical Integration Using the Composite Trapezoidal Rule
 *
 * Description:
 *   This program approximates the integral of the function
 *
 *         f(x) = 4.0/(1.0 + x*x)
 *
 *   on the interval [0, 1] using the composite trapezoidal rule.
 *
 *   The user is prompted to enter the number of subintervals (n) that should be used.
 *   The composite trapezoidal rule formula:
 *
 *         Integral ≈ h/2 * (f(a) + f(b)) + h * sum(f(a+i*h)) for i = 1 to n-1
 *
 *   is applied to compute the approximate integral.
 *
 *   Note:
 *     - Input: Number of subintervals n.
 *     - Output: Approximation of the integral (which approximates π).
 *   Compilation:
 *       gcc trapezoidal_rule.c -o program -lm
 */

#include <stdio.h>

// Function definition for f(x) = 4/(1+x*x)
double f(double x)
{
    return 4.0 / (1.0 + x * x);
}

int main()
{
    int i, n;         // 'i' is the loop counter, 'n' will be the number of subintervals.
    double a = 0.0;   // Lower limit of integration.
    double b = 1.0;   // Upper limit of integration.
    double h;         // The step size (length of each subinterval).
    double s = 0.0;   // Accumulator for the summation of function values.
    double x;         // A temporary variable for the current x value (not strictly necessary).

    // Prompt the user for the number of subintervals.
    printf("Enter number of subintervals, n = ");
    scanf("%d", &n);

    // Calculate the step size: h = (b - a) / n.
    h = (b - a) / n;

    // Compute the sum of f(a + i*h) for i from 1 to n-1.
    // These represent the interior points of the trapezoids.
    for (i = 1; i <= n - 1; i++) {
        s = s + f(a + i * h);
    }

    // Apply the composite trapezoidal rule:
    // Total integral approximation = (h/2) * [f(a) + f(b)] + h * s.
    s = h / 2 * (f(a) + f(b)) + h * s;

    // Print the computed approximate integral value with high precision.
    printf("%20.12f\n", s);

    return 0;
}
