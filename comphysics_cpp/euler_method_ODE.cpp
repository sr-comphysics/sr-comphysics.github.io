/*
 * Title: Euler's Method for Solving an Ordinary Differential Equation
 *
 * Description:
 * This program approximates the solution of an ordinary differential equation (ODE)
 * using Euler's method. The ODE in question is defined by:
 *
 *      dy/dx = 2xy
 *
 * Given an initial condition (x0, y0), the method calculates successive values of y
 * for increasing values of x using the formula:
 *
 *      y(next) = y(current) + h*f(x(current), y(current))
 *
 * where h is the x-increment and f(x, y) = 2xy. The program prompts the user for the
 * initial values, the step size (h), and the number of iterations (n) to perform.
 *
 * Compiler Note:
 * Compile the program with g++ using:
 *      g++ -o euler_method_ODE euler_method_ODE.cpp
 * This will compile the source code into an executable named "euler_method".
 */

#include <iostream>   // Provides input/output functionalities (cin, cout)
#include <iomanip>    // Provides manipulators like setprecision and setw for output formatting
#include <cmath>      // Provides mathematical functions (if needed)
using namespace std;  // Allows using standard library names without the "std::" prefix

// Function prototype for f(x, y), representing the right-hand side of the ODE dy/dx = 2xy.
double f(double x, double y);

int main()
{
    // Inform the user about the purpose of the program.
    cout << "Euler's method for solving a differential equation: \n";

    // Declare variables for current values of x and y, next x and y values, and step size h.
    double x, y, xNext, yNext, h;
    // Declare an integer for the number of iterations to perform.
    int n;

    // Prompt the user to enter initial values for x and y.
    cout << "Enter x0 and y0: \n";
    cin >> x >> y;

    // Prompt the user to enter the step size (x-increment).
    cout << "\nEnter value of x-increment to use: ";
    cin >> h;

    // Ask for the number of steps (or calculated values) desired.
    cout << "\nEnter the number of values to calculate: ";
    cin >> n;

    // Print the header for the output table.
    cout << "      X        Y\n"
         << "=====================\n"
         << fixed << setprecision(5)
         << showpoint;

    // Print the initial condition.
    cout << setw(10) << x << setw(10) << y << endl;

    // Loop over the number of iterations.
    for (int i = 1; i <= n; i++)
    {
        // Calculate the next x value by adding the step size.
        xNext = x + h;
        // Update y using Euler's method: y = y + h * f(x, y).
        y = y + f(x, y) * h;
        // Move forward to the next x value.
        x = xNext;
        // Output the current x and y values.
        cout << setw(10) << x << setw(10) << y << endl;
    }

    return 0;  // Indicate successful termination of the program.
}

// Function definition for f(x, y), representing the derivative dy/dx.
double f(double x, double y)
{
    // Return the evaluated derivative for the given x and y based on the ODE dy/dx = 2xy.
    return 2.0 * x * y;
}
