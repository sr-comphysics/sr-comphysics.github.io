/*
 * Title: Simpson's Rule for Approximating π
 *
 * Description:
 * This program uses Simpson's rule to numerically approximate the definite integral:
 *
 *             ∫[0,1] 4/(1+x*x) dx
 *
 * which is known to equal π. Simpson's rule is applied with the user-specified number
 * of partitions (which must be even) to compute the approximation.
 *
 * Simpson's rule formula:
 *   Integral ≈ (h/3) * [f(x0) + f(xn) + 4(f(x1)+ f(x3)+...) + 2(f(x2)+f(x4)+...)]
 *
 * Compiler Note:
 * To compile this program using gcc, use the following command:
 *    gcc -o simpsons_rule simpsons_rule.c -lm
 * The "-lm" flag is required to link the math library.
 */

#include <stdio.h>  // Provides standard input/output functionality
#include <math.h>   // Provides mathematical functions such as f() operations

// Function f(x) defined as 4/(1+x*x)
// For x in [0,1], the integral of f(x) gives the value of π.
double f(double x) {
    return 4.0 / (1.0 + x * x);
}

int main() {
    int i, n;               // 'i' for loop indexing and 'n' for number of partitions (must be even)
    double a = 0.0, b = 1.0;  // Integration limits: a = lower limit (0.0) and b = upper limit (1.0)
    double h;               // Step size (h)
    double s1 = 0.0, s2 = 0.0, s3 = 0.0; // s1, s2, s3 will accumulate the different summation components
    double x;               // Variable used for intermediate calculations (unused in final code but could be used for clarity)

    // Prompt user for the number of partitions, which must be even.
    printf("Enter number of partitions (must be even) = ");
    scanf("%d", &n);

    // Calculate the step size h.
    // Note: In Simpson's rule, the number of intervals = 2*n, so h = (b - a) / (2*n)
    h = (b - a) / (2.0 * n);

    // Calculate s1 which is the sum of the first and last terms:
    // f(a) and f(b)
    s1 = f(a) + f(b);

    // Calculate the sum of function values at odd indices: these will be multiplied by 4.
    // Loop index i goes from 1 to (2*n - 1) stepping by 2.
    for (i = 1; i < 2 * n; i += 2) {
        s2 += f(a + i * h);
    }

    // Calculate the sum of function values at even indices (except the first and last term):
    // These will be multiplied by 2.
    // Loop index i goes from 2 to (2*n - 2) stepping by 2.
    for (i = 2; i < 2 * n; i += 2) {
        s3 += f(a + i * h);
    }

    // Calculate the Simpson's rule approximation:
    // (h / 3) multiplied by the weighted sum:
    // s1 + 4*s2 + 2*s3
    printf("%lf\n", (h / 3.0) * (s1 + 4.0 * s2 + 2.0 * s3));

    return 0;  // Exit the program successfully
}
