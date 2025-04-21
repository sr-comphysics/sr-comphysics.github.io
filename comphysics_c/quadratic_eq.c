/* Program Title: Quadratic Equation Solver
 *
 * Description:
 *   This program computes the roots of a quadratic equation of the form:
 *
 *         ax² + bx + c = 0
 *
 *   The program prompts the user to enter the coefficients a, b, and c.
 *
 *   It calculates the discriminant as:
 *
 *         disc = b² - 4ac
 *
 *   - If the discriminant is negative, the program prints "Imaginary roots!".
 *   - Otherwise, it computes both roots using the quadratic formula:
 *              x1 = (-b + sqrt(disc)) / (2a)
 *              x2 = (-b - sqrt(disc)) / (2a)
 *
 *   Note:
 *     - Only real roots are computed when disc ≥ 0.
 *
 *   Compilation:
 *       gcc quadratic_eq.c -o program -lm
 *
 */

#include <stdio.h>
#include <math.h>

int main()
{
    double a, b, c;    // Coefficients of the quadratic equation.
    double disc;       // Discriminant: b² - 4ac.
    double x1, x2;     // Variables to store the roots.

    // Prompt the user to enter three coefficients (a, b, and c)
    printf("Enter 3 coeffs (separated by space) = ");
    scanf("%lf %lf %lf", &a, &b, &c);

    // Calculate the discriminant
    disc = b * b - 4 * a * c;

    // Check if the discriminant is negative
    if (disc < 0)
    {
        // If negative, the equation has imaginary roots
        printf("Imaginary roots !\n");
    }
    else
    {
        // Otherwise, compute both roots using the quadratic formula
        x1 = (-b + sqrt(disc)) / (2 * a);
        x2 = (-b - sqrt(disc)) / (2 * a);
        // Output the calculated roots
        printf("The roots are %lf, %lf.\n", x1, x2);
    }

    return 0;
}
