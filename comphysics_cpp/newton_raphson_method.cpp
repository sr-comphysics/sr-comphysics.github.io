/*
 * Title: Newton Raphson's Method for Solving a Nonlinear Equation Involving a Tangent Function
 *
 * Description:
 * This program applies Newton's method to solve a nonlinear equation defined by:
 *
 *      g(x) = x * tan(x) - sqrt(rho^2 - x^2) = 0
 *
 * where rho is a given constant. The derivative of g(x) is given by:
 *
 *      g'(x) = tan(x) + x / cos^2(x) + x / sqrt(rho^2 - x^2)
 *
 * The user is prompted to enter an initial guess x0. Newton's method is then used to
 * iteratively refine this guess. The iteration continues until the difference between
 * successive approximations is less than the tolerance eps, or until a maximum number of
 * iterations (nmax) is reached. At each iteration, the current approximation and the error
 * are printed.
 *
 * Compiler Note:
 * Compile this program using g++:
 *      g++ -o newton_raphson_method newton_raphson_method.cpp -lm
 * The "-lm" flag ensures the math library is linked for functions like tan(), sqrt(), and pow().
 */

#include <iostream>   // Provides input/output functionality (cin, cout)
#include <cmath>      // Provides mathematical functions (tan, sqrt, pow, fabs)
using namespace std;

int main()
{
    // Problem constants:
    // rho is a parameter in the equation.
    const double rho = 15.0;
    // Desired accuracy (tolerance for error)
    const double eps = 1.0e-6;
    // Maximum number of iterations allowed
    const int nmax = 1000;

    // Variables for current and updated iterates and the error estimate.
    double x0, x1, err, g, gp;
    int i;

    // Prompt the user for the initial guess x0.
    cout << "Enter x0: \n";
    cin >> x0;

    // Initialize error to a large value before starting iterations.
    err = 1.0;

    // Print header for the iteration output.
    cout << "Iteration          x                   Error   \n";
    cout << "================================================\n";
    cout << "   " << 0 << "         " << x0 << "                            " << err << "\n";

    // Set full precision for x values in subsequent outputs.
    cout.precision(17);

    // Begin Newton's method iterations up to nmax times.
    for (i = 1; i <= nmax; i++)
    {
        // Compute the function value at x0:
        // g(x) = x*tan(x) - sqrt(rho^2 - x^2)
        g = x0 * tan(x0) - sqrt(pow(rho, 2) - pow(x0, 2));

        // Compute the derivative g'(x) at x0:
        // g'(x) = tan(x) + (x / cos^2(x)) + (x / sqrt(rho^2 - x^2))
        gp = tan(x0) + x0 / pow(cos(x0), 2) + x0 / sqrt(pow(rho, 2) - pow(x0, 2));

        // Perform a single Newton's method update:
        // x1 = x0 - g(x0) / g'(x0)
        x1 = x0 - g / gp;

        // Calculate the absolute error between the new and current iterate.
        err = fabs(x1 - x0);

        // Print the iteration number, the current approximation, and the error.
        cout << "   " << i << "         " << x1 << "      " << err << "\n";

        // Check stopping condition: if error is below the tolerance, exit the loop.
        if (err < eps)
            break;

        // Update x0 for the next iteration.
        x0 = x1;
    }

    return 0;  // Return 0 to indicate successful program termination.
}
