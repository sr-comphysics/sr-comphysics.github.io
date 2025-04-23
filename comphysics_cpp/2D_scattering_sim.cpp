/* 
 * Title: 2D Scattering Simulation using Runge–Kutta Integration
 * Description:
 *   This program simulates a two-dimensional scattering experiment.
 *   A projectile moving in the plane is subjected to forces
 *   characterized by the coupling constants k1 and k2.
 *   Using a 4th-order Runge-Kutta integration method, the code
 *   computes the trajectory for given initial positions and velocities.
 *   The final scattering angle is computed from the asymptotic velocities.
 *
 *   Key simulation details:
 *     - Global Arrays: T[], X1[], X2[], V1[], and V2[] store the time,
 *       positions along x1 (horizontal) and x2 (vertical), and velocities.
 *     - k1: The primary coupling constant (e.g., gravitational effect).
 *     - k2: A secondary coupling constant reserved for other interactions.
 *     - Functions f1, f2, f3, f4:
 *         f1: returns v1 (dx1/dt)
 *         f2: returns v2 (dx2/dt)
 *         f3: returns 0.0 (currently no horizontal acceleration)
 *         f4: returns -k1 (vertical acceleration, e.g., gravity)
 *     - RKSTEP: Implements a complete RK4 time step.
 *     - RK: Integrates from initial time (Ti) to final time (Tf)
 *       with Nt steps, storing the integration history.
 */

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cmath>

using namespace std;

const int P = 1010000;           // Maximum number of integration points (array size)
double T[P], X1[P], X2[P], V1[P], V2[P];  // Global arrays to store simulation data over time
double k1, k2;                   // Coupling constants for the interactions

// f1: derivative of x1 (equals v1)
double f1(const double& t, const double& x1, const double& x2,
          const double& v1, const double& v2) {
    return v1;
}

// f2: derivative of x2 (equals v2)
double f2(const double& t, const double& x1, const double& x2,
          const double& v1, const double& v2) {
    return v2;
}

// f3: derivative of v1, horizontal acceleration
double f3(const double& t, const double& x1, const double& x2,
          const double& v1, const double& v2) {
    // Currently, no horizontal force is applied.
    return 0.0;
}

// f4: derivative of v2, vertical acceleration (e.g., gravitational acceleration)
double f4(const double& t, const double& x1, const double& x2,
          const double& v1, const double& v2) {
    return -k1;
}

// energy: Computes the total energy of the system (kinetic + potential)
double energy(const double& t, const double& x1, const double& x2,
              const double& v1, const double& v2) {
    return 0.5 * (v1 * v1 + v2 * v2) + k1 * x2;
}

// RKSTEP: Performs one RK4 integration step updating t, x1, x2, v1, and v2.
void RKSTEP(double &t, double &x1, double &x2, double &v1, double &v2,
            const double &dt) {
    // Compute k1 values
    double k1_x1 = dt * f1(t, x1, x2, v1, v2);
    double k1_x2 = dt * f2(t, x1, x2, v1, v2);
    double k1_v1 = dt * f3(t, x1, x2, v1, v2);
    double k1_v2 = dt * f4(t, x1, x2, v1, v2);

    // Compute k2 values at the midpoint
    double t_mid = t + dt / 2.0;
    double x1_mid = x1 + k1_x1 / 2.0;
    double x2_mid = x2 + k1_x2 / 2.0;
    double v1_mid = v1 + k1_v1 / 2.0;
    double v2_mid = v2 + k1_v2 / 2.0;
    double k2_x1 = dt * f1(t_mid, x1_mid, x2_mid, v1_mid, v2_mid);
    double k2_x2 = dt * f2(t_mid, x1_mid, x2_mid, v1_mid, v2_mid);
    double k2_v1 = dt * f3(t_mid, x1_mid, x2_mid, v1_mid, v2_mid);
    double k2_v2 = dt * f4(t_mid, x1_mid, x2_mid, v1_mid, v2_mid);

    // Compute k3 values at the midpoint again using k2
    x1_mid = x1 + k2_x1 / 2.0;
    x2_mid = x2 + k2_x2 / 2.0;
    v1_mid = v1 + k2_v1 / 2.0;
    v2_mid = v2 + k2_v2 / 2.0;
    double k3_x1 = dt * f1(t_mid, x1_mid, x2_mid, v1_mid, v2_mid);
    double k3_x2 = dt * f2(t_mid, x1_mid, x2_mid, v1_mid, v2_mid);
    double k3_v1 = dt * f3(t_mid, x1_mid, x2_mid, v1_mid, v2_mid);
    double k3_v2 = dt * f4(t_mid, x1_mid, x2_mid, v1_mid, v2_mid);

    // Compute k4 values at the end of the interval
    double t_end = t + dt;
    double x1_end = x1 + k3_x1;
    double x2_end = x2 + k3_x2;
    double v1_end = v1 + k3_v1;
    double v2_end = v2 + k3_v2;
    double k4_x1 = dt * f1(t_end, x1_end, x2_end, v1_end, v2_end);
    double k4_x2 = dt * f2(t_end, x1_end, x2_end, v1_end, v2_end);
    double k4_v1 = dt * f3(t_end, x1_end, x2_end, v1_end, v2_end);
    double k4_v2 = dt * f4(t_end, x1_end, x2_end, v1_end, v2_end);

    // Update each variable with the weighted sum of the increments
    x1 += (k1_x1 + 2.0*k2_x1 + 2.0*k3_x1 + k4_x1) / 6.0;
    x2 += (k1_x2 + 2.0*k2_x2 + 2.0*k3_x2 + k4_x2) / 6.0;
    v1 += (k1_v1 + 2.0*k2_v1 + 2.0*k3_v1 + k4_v1) / 6.0;
    v2 += (k1_v2 + 2.0*k2_v2 + 2.0*k3_v2 + k4_v2) / 6.0;
    t  += dt;
}

// RK: Integrates the system for Nt steps from Ti to Tf using RKSTEP.
// The state history from the integration is stored in the global arrays.
void RK(const double &Ti, const double &Tf, const double &X10,
        const double &X20, const double &V10, const double &V20,
        const int &Nt) {
    // Set initial conditions in arrays.
    T[0] = Ti;
    X1[0] = X10;
    X2[0] = X20;
    V1[0] = V10;
    V2[0] = V20;

    double dt = (Tf - Ti) / Nt;
    double t = Ti, x1 = X10, x2 = X20, v1 = V10, v2 = V20;

    // Integration loop for each time step.
    for (int i = 1; i < Nt; i++) {
        RKSTEP(t, x1, x2, v1, v2, dt);
        T[i] = t;
        X1[i] = x1;
        X2[i] = x2;
        V1[i] = v1;
        V2[i] = v2;
    }
}

int main() {
    string buf;
    double Ti, Tf, X10, X20, V10, V20;
    double X20F, dX20;
    int Nt, i;
    const int Nbins = 20;         // Number of bins for the angular distribution.
    int index;
    double angle, bins[Nbins], Npart;
    const double pi = 3.14159265358979324;
    const double rad2deg = 180.0 / pi;
    const double dangle = pi / Nbins;
    double R, density, dOmega, sigma, sigmatot;

    // Prompt for input parameters.
    cout << "Runge-Kutta Method for 4-ODEs Integration\n";
    cout << "Enter coupling constants (k1 and k2): \n";
    cin >> k1 >> k2;
    getline(cin, buf);  // clear newline

    cout << "k1 = " << k1 << "   k2 = " << k2 << "\n";
    cout << "Enter Nt, Ti, Tf, X10, X20, V10, V20: \n";
    cin >> Nt >> Ti >> Tf >> X10 >> X20 >> V10 >> V20;
    getline(cin, buf);

    cout << "Enter final impact parameter X20F and step dX20: \n";
    cin >> X20F >> dX20;

    // Display the simulation settings.
    cout << "Nt = " << Nt << "\n";
    cout << "Time: Initial Ti = " << Ti << "  Final Tf = " << Tf << "\n";
    cout << "X1(Ti) = " << X10 << "   X2(Ti) = " << X20 << "\n";
    cout << "V1(Ti) = " << V10 << "   V2(Ti) = " << V20 << "\n";
    cout << "Impact parameter: initial X20 = " << X20 << "  final X20F = " << X20F
         << "  dX20 = " << dX20 << "\n";

    // Open output file.
    ofstream myfile("scatter.dat");
    if (!myfile) {
        cerr << "Error opening file for writing.\n";
        return EXIT_FAILURE;
    }
    myfile.precision(17);

    // Initialize bins to zero.
    for (i = 0; i < Nbins; i++) {
        bins[i] = 0.0;
    }
    Npart = 0.0;

    // Adjust initial impact parameter X20 by half a step to center the first interval.
    X20 = X20 + dX20 / 2.0;

    // Loop over impact parameters.
    while (X20 < X20F) {
        RK(Ti, Tf, X10, X20, V10, V20, Nt);

        // Compute the scattering angle based on final velocities.
        angle = abs(atan2(V2[Nt - 1], V1[Nt - 1]));

        // Write data for the current impact parameter:
        // current impact parameter, final angle, an angle at an earlier step, and a derived quantity.
        myfile << "@" << X20 << " " << angle << " "
               << abs(atan2(V2[Nt - 51], V1[Nt - 51])) << " "
               << k1 / (V10 * V10) / tan(angle / 2.0) << "\n";

        // Bin the scattering angle.
        index = int(angle / dangle);
        if(index >= 0 && index < Nbins) {
            bins[index] += X20;
        }
        Npart += X20;
        X20 += dX20; // Increment the impact parameter.
    }

    // Density, total cross section calculations.
    R = X20;
    density = Npart / (pi * R * R);
    sigmatot = 0.0;
    for (i = 0; i < Nbins; i++) {
        angle = (i + 0.5) * dangle; // Central angle of the bin.
        dOmega = 2.0 * pi * sin(angle) * dangle; // Solid angle element.
        sigma = bins[i] / (density * dOmega);
        if (sigma > 0.0)
            myfile << "ds= " << angle << " " << angle * rad2deg << " " << sigma << "\n";
        sigmatot += sigma * dOmega;
    }
    myfile << "sigmatot= " << sigmatot << "\n";
    myfile.close();

    cout << "Simulation complete. Results written to scatter.dat\n";

    // Optional pause to view console output before closing (Windows system)
    // system("pause");
    return 0;
}
