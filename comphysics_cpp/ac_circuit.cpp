/*
 * Title: AC Circuit Analysis: Impedance and Current Calculation
 *
 * Description:
 * This program computes the current in an AC circuit consisting of a resistor (R),
 * an inductor (L), and a capacitor (C) when subjected to an AC voltage. The circuit's
 * impedance (Z) is computed using the formula:
 *
 *      Z = R + j*(w*L) - j/(w*C)
 *
 * where j is the imaginary unit and w is the angular frequency in radians per second.
 * The user is prompted to enter the circuit parameters (R, L, C), the frequency of the source,
 * and a complex voltage V (in the form: (real, imaginary)). The current (I) is then computed as:
 *
 *      I = V / Z
 *
 * The program outputs the current in rectangular form along with its magnitude.
 *
 * Compiler Note:
 * Compile this program using g++ with:
 *      g++ -o ac_circuit ac_circuit.cpp -lm
 * The "-lm" flag links the math library for mathematical functions such as abs().
 */

#include <iostream>     // Provides input/output functionality (cin, cout)
#include <complex>      // Provides complex number support using the complex template
#include <iomanip>      // Provides manipulators for formatted output (setprecision, setw)
#include <cmath>        // Provides mathematical functions (abs, etc.)

using namespace std;    // Allows usage of standard library names without the "std::" prefix

int main()
{
    // Define the imaginary unit 'i' as a complex number (0, 1)
    const complex<double> i(0, 1);

    // Declare variables for the circuit parameters and angular frequency
    double R, L, C, w;
    // Declare complex variables for the voltage (V), impedance (Z), and current (I)
    complex<double> V, Z, I;

    // Prompt user for resistance, inductance, and capacitance values
    cout << "\nEnter the resistance (ohms), inductance (henries), and capacitance (farads): \n";
    cin >> R >> L >> C;

    // Prompt user for the frequency in cycles per second (assumed to represent angular frequency)
    cout << "\nEnter the frequency (cycles/second): ";
    cin >> w;

    // Check to ensure that both frequency and capacitance are non-zero to avoid division by zero
    if (w == 0.0 || C == 0.0) {
        cout << "\nFrequency (w) and capacitance (C) must be non-zero to compute the impedance.\n";
        return 1;
    }

    // Prompt user to input the voltage as a complex number in the form (real, imaginary)
    cout << "\nEnter voltage as a complex number in the form (x, y): ";
    cin >> V;

    // Calculate the circuit impedance using the formula:
    // Z = R + j*(w*L) - j/(w*C)
    Z = R + (w * L * i) - (i / (w * C));

    // Calculate the current using Ohm's law for AC circuits: I = V / Z
    I = V / Z;

    // Output the computed current in rectangular form and its magnitude
    cout << fixed << setprecision(2)
         << "\nCurrent = " << real(I) << " + " << imag(I) << "I"
         << "\nwith magnitude = " << abs(I) << endl;

    return 0;  // Terminate the program successfully
}
