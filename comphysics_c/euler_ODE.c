/* Program Title: Euler’s Method for a System of Differential Equations
 *
 * Description:
 * This program approximates a solution to a simple system of differential equations using
 * Euler’s method. The system of ODEs solved is:
 *
 *  dy₁/dx = y₂
 *  dy₂/dx = -y₁
 *
 * The initial conditions are:
 *  y₁ = 0.0 and y₂ = 1.0 at x = 0.0.
 *
 * In this example, only a single step with step size h = 0.01 is computed.
 *
 * The output prints the current value of x, the computed y₂ value, and cos(x) (as comparison,
 * since the exact solution for y₂ is cos(x) for this system given the initial conditions).
 *
 * Note:
 *   - To compile this program, a standard math library is needed, so use the -lm flag:
 *         gcc euler_ODE.c -o program -lm
 *
 */

#include <stdio.h>
#include <math.h>

// Function f1 : Represents the derivative dy₁/dx = y₂.
// Inputs: current value of x, y1, and y2.
// Returns: the derivative y₂.
double f1(double x, double y1, double y2) {
    return y2;
}

// Function f2 : Represents the derivative dy₂/dx = -y₁.
// Inputs: current value of x, y1, and y2.
// Returns: the derivative -y₁.
double f2(double x, double y1, double y2) {
    return -y1;
}

int main()
{
    // Define step size h. A small step h is used for Euler's method.
    double h = 0.01;

    // Variables to store the approximate values of y₁ and y₂.
    double y1, y2;

    // Variable for the current value of x.
    double x;

    // Loop counter for iterations.
    int i;

    // Set initial conditions: y₁(0) = 0 and y₂(0) = 1, at x = 0.
    y1 = 0.0;
    y2 = 1.0;
    x  = 0.0;

    // Print header for output.
    // The output will display x, the computed y₂, and cos(x) which is the exact solution for y₂.
    printf("x\t y2 (approx.)\t cos(x)\n");

    // For this program, we only compute one iteration.
    // Typically, you might run this for multiple steps to see how the solution evolves.
    for (i = 0; i <= 0; i++)
    {
        // Print the current values of x, y2 (approximation), and cos(x) (exact solution).
        printf("x = %f\t y2 = %f\t cos(x) = %f\n", x, y2, cos(x));

        // Euler's method to update y₁ and y₂:
        // New y1 = current y1 + h * f1(x, y1, y2)
        y1 = y1 + h * f1(x, y1, y2);

        // New y2 = current y2 + h * f2(x, y1, y2)
        // Note: in a more sophisticated method, you might use the previous value of y1 for this update.
        // Here, the update is done sequentially, which is typical for Euler’s method.
        y2 = y2 + h * f2(x, y1, y2);

        // Increase x by the step size h.
        x  = x + h;
    }

    // End of program.
    return 0;
}
