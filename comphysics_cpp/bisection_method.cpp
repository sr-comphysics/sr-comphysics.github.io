/* Title: Root Finding via the Bisection Method
 *
 * Description:
 * This program approximates a solution (i.e., a root) for a nonlinear equation of the
 * form f(x) = 0 using the bisection method. The function f(x) is defined as:
 *
 *     f(x) = x^3 + x - 5
 *
 * The user is first prompted to specify the desired accuracy for the approximation.
 * Then the program repeatedly asks for an interval [x1, x2] where the function f(x)
 * changes sign (i.e., f(x1)*f(x2) < 0), ensuring that at least one root exists within
 * the interval. The bisection method is then employed to iteratively halve the interval
 * until the half-width of the interval is less than the specified accuracy. The x3point of
 * the final interval is output as the approximate solution.
 *
 * Compiler Note:
 * Compile this program using g++ as follows:
 *      g++ -o bisection_method bisection_method.cpp
 */

#include <iostream>   // Provides input/output functionality (cin, cout)
#include<cmath>     // Provides mathematical functions (e.g., sqrt, pow)
using namespace std;

// Function prototype for f(x) used in the root-finding process.
double f(double x);

int main()
{
    // Declare a variable to hold the desired accuracy.
    double accu;
    // Prompt user for the accuracy (e.g., 0.01 or 1e-2).
    cout << "\nEnter the accuracy desired (e.g. .01 or 1e-2): ";
    // Read the accuracy value from input.
    cin >> accu;

    // Declare variables to store the endpoints of the interval.
    double x1, x2;

    // Continuously prompt the user for an interval that contains a root.
    // This loop ensures f(x1) and f(x2) have opposite signs.
    do
    {
        cout << "Enter endpoints of an interval containing a solution: \n";
        cin >> x1 >> x2;
    }
    while (f(x1) * f(x2) >= 0.0);

    // Initialize the width of the interval and declare variables for the midpoint (x3)
    // and the function value at the midpoint (f_x3).
    double width = x2 - x1, x3, f_x3;

    // Continue halving the interval until the half-width is less than the specified accuracy.
    while (width / 2.0 > accu)
    {
        // Compute the x3point of the current interval.
        x3 = (x1 + x2) / 2.0;
        // Evaluate the function at the midpoint (f_x3).
        f_x3 = f(x3);

        // Determine which subinterval contains a sign change, and hence the root:
        // If f(x1) and f(x3) have opposite signs, the root lies in [x1, x3].
        if (f(x1) * f_x3 < 0.0)
            x2 = x3;  // Narrow the interval to [x1, x3].
        else
            x1 = x3;   // Otherwise, the root lies in [x3, x2]; narrow the interval.

        // Halve the width after updating the endpoints.
        width /= 2.0;
    }

    // Output the approximate solution (the x3point of the final interval)
    // along with the accuracy to which it is computed.
    cout << "\n-->" << x3 << " is an approximate solution of "
         << "f(x) = 0, to within " << accu << endl;

    return 0;  // Terminate the program successfully.
}

// Definition of the function f(x):
// f(x) = x^3 + x - 5, which models the nonlinear equation to be solved.
double f(double x)
{
    return pow(x, 3) + x - 5;
}
