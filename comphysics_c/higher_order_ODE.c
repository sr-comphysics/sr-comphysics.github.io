/*
 * Title: Numerical Integration of a Second-Order Oscillator using Euler's Method
 *
 * Description:
 * This program uses Euler's method to numerically integrate a system of two
 * coupled ordinary differential equations representing a simple harmonic oscillator.
 *
 * The system of ODEs is:
 *      dy1/dx = y2
 *      dy2/dx = -y1
 *
 * with the initial conditions:
 *      y1(0) = 0, y2(0) = 1.
 *
 * The exact solution for this system is:
 *      y1 = sin(x)  and  y2 = cos(x)
 * which is used for comparison in the output.
 *
 * The integration is performed with a fixed step size h = 0.01 and for 11 steps,
 * printing the current value of x, the numerical solution for y2, and the exact value cos(x).
 *
 * Compiler Note:
 *
 * To compile this program using gcc, execute the following command:
 *    gcc -o higher_order_ODE higher_order_ODE.c -lm
 *
 * The "-lm" option links the math library, which is required for functions such as cos() 
 * and sin(). Make sure your compiler supports C99 or later.
 */

#include <stdio.h>   // Provides input/output functions (printf)
#include <math.h>    // Provides mathematical functions (cos)

// Function f1 computes the derivative dy1/dx = y2.
// Parameters:
//   x  - the independent variable (unused in this function)
//   y1 - the current value of y1 (unused in this function, but included for consistency)
//   y2 - the current value of y2, which is dy1/dx
double f1(double x, double y1, double y2) {
    return y2;
}

// Function f2 computes the derivative dy2/dx = -y1.
// Parameters:
//   x  - the independent variable (unused in this function)
//   y1 - the current value of y1, used to compute the derivative of y2
//   y2 - the current value of y2 (unused in this function, but included for consistency)
double f2(double x, double y1, double y2) {
    return -y1;
}

int main() {
    double h = 0.01;    // Declare and initialize the integration step size.
    double y1, y2, x;   // Declare variables for the state (y1 and y2) and the independent variable x.
    int i;              // Loop counter for the iterations.

    // Set initial conditions:
    y1 = 0.0;   // y1(0) = 0.0 (exact solution: sin(0) = 0)
    y2 = 1.0;   // y2(0) = 1.0 (exact solution: cos(0) = 1)
    x = 0.0;    // Initial value of the independent variable x.

    // Print a header for the output columns.
    printf("        x         y2 (num)     cos(x) (exact)\n");

    // Perform 11 iterations using Euler's method (from i=0 to i=10)
    for (i = 0; i <= 10; i++) {
        // Print the current values:
        // x     - the current independent variable,
        // y2    - the numerical approximation for y2 (which should approximate cos(x)),
        // cos(x) - the exact value of cos(x) for comparison.
        printf("x = %lf    %lf    %lf\n", x, y2, cos(x));
        
        // Update y1 using Euler's method:
        // new y1 = current y1 + h * f1(x, y1, y2)
        y1 = y1 + h * f1(x, y1, y2);

        // Update y2 using Euler's method:
        // new y2 = current y2 + h * f2(x, y1, y2)
        y2 = y2 + h * f2(x, y1, y2);

        // Increment the independent variable x by the step size h.
        x = x + h;
    }

    return 0;  // End the program successfully.
}
