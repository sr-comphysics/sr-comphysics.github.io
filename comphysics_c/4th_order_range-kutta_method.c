/* Title: Numerical Integration of dy/dt = y using the Fourth-Order Runge-Kutta Method (RK4)
 *
 * Description:
 * This program implements the classical fourth-order Runge-Kutta (RK4) method to
 * numerically solve the ordinary differential equation (ODE):
 *
 *      dy/dt = y
 *
 * with the initial condition:
 *
 *      y(0) = 1
 *
 * The exact solution of the ODE is y = exp(t), and this is used to compare the
 * accuracy of the RK4 numerical approximation. The program uses a fixed step size
 * of h = 0.1 and performs 11 iterations (from t = 0 to t = 1). For each step,
 * it computes four slopes (k1, k2, k3, k4) and updates the value of y accordingly.
 *
 * Compiler Note:
 * Use the following command to compile this program with gcc:
 *      gcc -o 4th_order_range-kutta_method 4th_order_range-kutta_method.c -lm
 * The "-lm" flag links the math library for the exp() function.
 */

#include <stdio.h>   // Provides input/output functions (e.g., printf)
#include <math.h>    // Provides mathematical functions (e.g., exp())

// Function f implements the right-hand side of the ODE: dy/dt = y.
double f(double t, double y)
{
    return y;  // For this ODE, f(t, y) = y.
}

int main()
{
    // Declare and initialize variables.
    double h = 0.1;   // Step size for the integration.
    double t, y;      // Variables to represent time (t) and the solution (y).
    double k1, k2, k3, k4;  // Variables to store the four slopes for RK4.
    int i;            // Loop counter.

    t = 0.0;  // Initialize time t to 0.0.
    y = 1.0;  // Set the initial condition: y(0) = 1.

    // Perform 11 iterations (from i = 0 to 10) which leads to t = 1.0 at the last step.
    for (i = 0; i <= 10; i++)
    {
        // Print current values:
        // t: current time,
        // y: RK4 approximation of the solution,
        // exp(t): exact solution computed as e^(t).
        printf("t = %lf  rk = %lf  exact = %lf \n", t, y, exp(t));

        /*
         * Compute the four intermediate slopes used in RK4:
         * k1: Slope at the beginning of the interval.
         * k2: Slope at the mid-point using k1.
         * k3: Slope at the mid-point using k2.
         * k4: Slope at the end of the interval.
         */

        // Calculate k1 based on the current state.
        k1 = h * f(t, y);
        // Calculate k2: estimate at the midpoint using k1.
        k2 = h * f(t + h/2, y + k1/2.0);
        // Calculate k3: another midpoint estimate using k2.
        k3 = h * f(t + h/2, y + k2/2.0);
        // Calculate k4: estimate at the end of the interval using k3.
        k4 = h * f(t + h, y + k3);

        // Update y using the weighted average of the four slopes.
        // The RK4 update formula is: y(new) = y(old) + (k1 + 2*k2 + 2*k3 + k4) / 6.
        y = y + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;

        // Increment time by the step size h.
        t = t + h;
    }

    return 0;  // Return 0 to indicate successful execution.
}
