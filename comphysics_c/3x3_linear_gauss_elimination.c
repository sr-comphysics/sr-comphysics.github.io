/* Program Title: Gaussian Elimination for Solving a 3x3 Linear System
 *
 * Description:
 *   This program solves a system of three linear equations in three unknowns
 *   using an elimination process similar to Gaussian elimination.
 *
 *   The augmented matrix 'a' (of size N x (N+1)) is defined as:
 *
 *         2   -1    1  |   2
 *        -1    3    3  |   3
 *         2    1    4  |   1
 *
 *   The program first performs forward elimination (with partial normalization)
 *   to transform the matrix. Then, back substitution is performed to find the
 *   unique solution vector for the system.
 *
 *   Note:
 *    - The code assumes N is 3.
 *    - Compile using: gcc 3x3_linear_gauss_elimination.c -o program -lm
 *
 */

#include <stdio.h>
#define N 3  // Define the number of equations/unknowns.

int main()
{
    // Define the augmented matrix for the system.
    // Each row represents one equation and the last column represents the RHS.
    double a[N][N+1] = {
        {2, -1,  1, 2},
        {-1, 3,  3, 3},
        {2,  1,  4, 1}
    };

    int i, j, k, l;

    // Normalize the first row (row 0) for columns 1 to N.
    for (j = 1; j < N+1; j++) {
        a[0][j] = a[0][j] / a[0][0];
    }

    // Forward elimination: eliminate the variables one pivot at a time.
    for (k = 1; k < N; k++) {
        // Adjust the k-th column of rows k to N-1 using previous pivot rows.
        for (i = k; i < N; i++) {
            for (l = 0; l < k; l++) {
                a[i][k] = a[i][k] - a[i][l] * a[l][k];
            }
        }

        // Update the remaining entries in the pivot row k (columns k+1 to N for RHS).
        for (j = k+1; j < N+1; j++) {
            // Adjust using the contributions from previous pivot rows.
            for (l = 0; l < k; l++) {
                a[k][j] = a[k][N] - a[k][l] * a[l][j];
            }
            // Normalize by the pivot element a[k][k].
            a[k][j] = a[k][j] / a[k][k];
        }
    }

    // Back Substitution:
    // From the last row up to the first row, adjust the RHS by subtracting the contributions
    // of already determined variables.
    for (k = N - 1; k >= 0; k--) {
        for (l = k + 1; l < N; l++) {
            a[k][N] = a[k][N] - a[k][l] * a[l][N];
        }
    }

    // Print the solution for each variable.
    for (i = 0; i < N; i++) {
        printf("x[%d] = %lf\n", i, a[i][N]);
    }

    return 0;
}
