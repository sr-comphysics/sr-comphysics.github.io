/*
 * Title: Quadratic Equation Solver Using the Discriminant
 *
 * Description:
 * This program calculates the roots of a quadratic equation of the form:
 *
 *      a*x^2 + b*x + c = 0
 *
 * The user is prompted to input the coefficients a, b, and c. The program first
 * asserts that a is non-zero because a zero coefficient would make the equation
 * linear rather than quadratic. It then computes the discriminant:
 *
 *      discriminant = b^2 - 4*a*c
 *
 * If the discriminant is non-negative, the program calculates the two real roots
 * using the quadratic formula:
 *
 *      x1 = (-b + sqrt(discriminant)) / (2*a)
 *      x2 = (-b - sqrt(discriminant)) / (2*a)
 *
 * If the discriminant is negative, the equation has no real roots and only complex ones,
 * which this program does not handle.
 *
 * Compiler Note:
 * Compile this program using g++ as follows:
 *      g++ -o quadratic_solver quadratic_solver.cpp -lm
 * The "-lm" flag links the math library for the sqrt() function.
 */

#include <iostream>   // Provides input/output functionality (e.g., cout, cin)
#include <cassert>    // Provides the assert() function to perform runtime assertions
#include <cmath>      // Provides mathematical functions (e.g., sqrt)

using namespace std;  // Allow use of standard library names without the "std::" prefix

int main()
{
    // Declare variables to store the coefficients of the quadratic equation.
    double a, b, c;

    // Prompt the user to enter the coefficients for the quadratic equation.
    cout << "Enter the coefficients of a quadratic equation (a, b, c): \n";

    // Read the coefficients from the user input.
    cin >> a >> b >> c;

    // Ensure that coefficient 'a' is not zero, otherwise the equation is not quadratic.
    assert(a != 0); // Runtime check: if a == 0, the program terminates with an assertion failure.

    // Calculate the discriminant using the formula: b^2 - 4*a*c.
    double disc = b * b - 4 * a * c, x1, x2;

    // Check if the discriminant is non-negative, which guarantees real roots.
    if (disc >= 0)
    {
        // Calculate the first root using the quadratic formula.
        x1 = (-b + sqrt(disc)) / (2 * a);
        // Calculate the second root using the quadratic formula.
        x2 = (-b - sqrt(disc)) / (2 * a);

        // Output the computed roots.
        cout << "x1 = " << x1 << " and " << "x2 = " << x2 << endl;
        cout << x1 << " or " << x2 << " are the roots.";
    }
    else
        // If the discriminant is negative, inform the user that there are no real roots.
        cout << "There are no real roots, only complex ones" << endl;

    return 0;  // Return 0 to indicate successful program termination.
}
