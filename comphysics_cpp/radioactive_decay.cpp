/*
 * Title: Radioactive Substance Decay Calculator
 *
 * Description:
 * This program calculates the remaining amount of a radioactive substance
 * after a given time period based on its half-life decay formula. The user is
 * prompted to enter the substance name, its half-life (in days), the initial amount
 * (in mg), and a time period (in days). The computation utilizes the formula:
 *
 *     amount_remaining = initial_amount * (0.5)^(time / half_life)
 *
 * which determines how much of the substance remains after the specified time period.
 *
 * Compiler Note:
 * Use the following command to compile this program with g++:
 *      g++ -o radioactive_decay radioactive_decay.cpp
 * This command compiles the C++ source code into an executable named "radioactive_decay".
 */

#include <iostream>   // Provides input/output functionality (e.g., cout, cin)
#include <string>     // Provides the std::string data type for handling text.
#include <cmath>      // Provides mathematical functions (e.g., pow)

using namespace std;  // Allows using names from the std namespace without the "std::" prefix.

int main() {
    // Prompt the user to enter the name of the radioactive substance.
    cout << "Enter the name of your radioactive substance: ";
    // Declare a variable "element" to hold the substance name.
    string element;
    // Read the substance name from the user input.
    cin >> element;

    // Prompt the user to enter the half-life of the substance in days.
    cout << "and its half-life (days): ";
    // Declare a variable "half_life" to store the half-life duration.
    double half_life;
    // Read the half-life value from the user input.
    cin >> half_life;

    // Prompt the user to enter the initial amount (in mg) and a time period (in days).
    cout << "Enter the initial amount (mg) and a time period (days): ";
    // Declare variables "initial_amount" and "time" for the starting mass and duration.
    double initial_amount, time;
    // Read both the initial amount and the time period from the user input.
    cin >> initial_amount >> time;

    // Calculate the remaining amount using the half-life decay formula.
    // The formula applied is: amount_remaining = initial_amount * pow(0.5, time/half_life);
    double amount_remaining = initial_amount * pow(0.5, time / half_life);

    // Output the result, detailing the substance, its half-life, the initial amount,
    // the remaining amount, and the time elapsed.
    cout << "\nFor " << element << " with half-life " << half_life << " days\n "
         << initial_amount << "mg " << " will be reduced to "
         << amount_remaining << " mg after " << time << " days\n";

    return 0;  // End of program execution. Return 0 to indicate successful completion.
}
