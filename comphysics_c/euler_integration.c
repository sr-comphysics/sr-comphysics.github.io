/*
 * Title: Numerical Integration of a 3D Dynamical System using Euler's Method
 *
 * Description:
 * This program uses Euler's method to numerically integrate a system
 * of three coupled ordinary differential equations (ODEs). The system is defined by:
 *
 *   du/dt = P * (v - u)
 *   dv/dt = -u * w + R * u - v
 *   dw/dt = u * v - b * w
 *
 * where the constants are defined as:
 *   P = 16.0, b = 4.0, R = 35.0.
 *
 * The initial conditions are:
 *   t = 0.0, u = 5.0, v = 5.0, w = 5.0
 * and the step size is h = 0.01.
 *
 * The program performs 3000 iterations of Euler's method, updating the state
 * variables at each time step, and prints the values of u and w.
 *
 * Compiler Note:
 * To compile this program using gcc, use the following command:
 *    gcc -o euler_integration euler_integration.c -lm
 * The "-lm" flag is generally included for math functions (if needed in future extensions).
 */

#include <stdio.h>  // Provides standard input/output functionality

// Define constants used in the system of differential equations.
#define P 16.0
#define b 4.0
#define R 35.0

// Function f1 corresponding to the differential equation: du/dt = P*(v - u)
double f1(double u, double v, double w) {
    return P * (v - u);
}

// Function f2 corresponding to the differential equation: dv/dt = -u*w + R*u - v
double f2(double u, double v, double w) {
    return -u * w + R * u - v;
}

// Function f3 corresponding to the differential equation: dw/dt = u*v - b*w
double f3(double u, double v, double w) {
    return u * v - b * w;
}

int main() {
    double h, t, u, v, w;  // Declare step size h, time t, and state variables u, v, w
    int i;                 // Loop index

    /* initial values */
    t = 0.0;      // Initial time
    h = 0.01;     // Time step size
    u = 5.0;      // Initial value for u
    v = 5.0;      // Initial value for v
    w = 5.0;      // Initial value for w

    // Euler's method: iterate 3000 times to update the variables using the differential equations
    for (i = 0; i < 3000; i++) {
        // Update u, v, and w using Euler integration:
        // new_value = old_value + step_size * derivative_at_old_value
        u = u + h * f1(u, v, w);
        v = v + h * f2(u, v, w);
        w = w + h * f3(u, v, w);

        // Print the current values of u and w at each time step.
        // (You may modify the printed variables as needed.)
        printf("%lf %lf\n", u, w);

        // Update time variable
        t = t + h;
    }

    return 0; // Terminate the program successfully
}
