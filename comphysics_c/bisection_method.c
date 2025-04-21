/* Program Title: Bisection Method for Approximating √2
 *
 * Description:
 * This program uses the bisection method to approximate the square root of 2 by finding a
 * root of the function f(x) = x^2 - 2. The bisection method works by repeatedly halving an
 * interval that is known to contain a root until the interval is sufficiently small.
 *
 * Steps:
 *  1. The program prompts the user to enter two endpoints (xleft and xright) of an interval
 *     where the function changes sign (i.e., f(xleft)*f(xright) < 0).
 *  2. It computes the midpoint of the interval.
 *  3. Based on the sign of the function at the midpoint, the program determines in which subinterval
 *     the root lies and updates the interval accordingly.
 *  4. The process repeats until the absolute difference between the endpoints is less than a small
 *     tolerance (EPS), or if the midpoint is an exact root.
 *  5. The program prints the number of iterations performed and the approximate value of the root.
 *
 * Compilation Note:
 * If compiling via the command line (using gcc), link the math library with the -lm flag:
 *      gcc bisection.c -o bisection -lm
 *
 */

#include <stdio.h>
#include <math.h>

// Define a very small number for convergence check (tolerance)
#define EPS 1.0e-10

// Define the maximum number of iterations allowed
#define N 100

// Function: f(x) = x^2 - 2
// The root of this function corresponds to the square root of 2.
double f(double x)
{
    return pow(x, 2) - 2;
}

int main()
{
    double x1, x2, x3;  // Variables for interval endpoints (x1, x2) and the midpoint (x3)
    int count;          // Variable to keep track of the iteration count

    // Step 1: Request user input for an interval that brackets the root.
    // The bisection method requires that f(x1) and f(x2) have opposite signs.
    do
    {
        printf("Enter xleft and xright separated by space = ");
        // Read double values for x1 and x2.
        scanf("%lf %lf", &x1, &x2);
    }
    while (f(x1) * f(x2) > 0);   // Repeat input prompt until a valid interval is provided.

    // Step 2: Perform the bisection iterations (up to a maximum of N iterations).
    for (count = 0; count < N; count++)
    {
        // Compute the midpoint x3 of the current interval [x1, x2]
        x3 = (x1 + x2) / 2.0;

        // Step 3: Determine in which subinterval the root lies by checking the sign of the function.
        // If f(x1) and f(x3) have opposite signs, the root is in the interval [x1, x3].
        // Otherwise, the root must be in the interval [x3, x2].
        if (f(x1) * f(x3) < 0)
            x2 = x3;  // Update the right endpoint to the midpoint.
        else
            x1 = x3;  // Update the left endpoint to the midpoint.

        // Step 4: Check for convergence.
        // Either an exact root is found (f(x3) == 0) or the interval size is less than the tolerance EPS.
        if (f(x3) == 0.0 || fabs(x1 - x2) < EPS)
            break;  // Exit the loop if the desired precision is achieved.
    }

    // Step 5: Output the results.
    // Print the number of iterations taken and the approximated value for √2.
    printf("Iteration = %d\n", count);
    printf("x = %f\n", x1);

    // End of program.
    return 0;
}
