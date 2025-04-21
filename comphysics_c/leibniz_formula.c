/*
 * Title: Leibniz Formula for π Approximation
 *
 * Description:
 * This program approximates the value of π using the Leibniz series.
 * The Leibniz series for π is given by:
 *
 *               π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ... 
 *
 * The program computes an approximation by summing the first 1000 terms of this series,
 * then prints both the computed approximation and the exact value computed using the 
 * standard library function atan(1.0) (since atan(1.0) = π/4).
 *   Note:
 *    - Compile using: gcc leibniz_formula.c -o program -lm
 *
 */

#include <stdio.h>  // Include standard I/O functions for input and output operations
#include <math.h>   // Include math library for pow and atan functions

int main() {
    int i;                     // Declare variable i for loop indexing
    double sum = 0.0;          // Initialize sum to store the running total of the series

    // Loop through the first 1000 terms of the Leibniz series (Increase the number of terms to get the more precise value)
    for (i = 0; i < 1000; i++) {
        // pow(-1, i) alternates the sign for each term: positive when i is even, negative when odd.
        // denominator is (2 * i + 1) to account for the odd integers in the series.
        sum += pow(-1, i) / (double)(2 * i + 1);
    }

    // Multiply the sum by 4 to estimate π
    // Compare the approximation with the exact value obtained from 4 * atan(1.0) because atan(1.0) = π/4.
    printf("approx= %lf\nexact value= %lf.\n", 4 * sum, 4 * atan(1.0));

    return 0;  // End of program with successful termination
}
