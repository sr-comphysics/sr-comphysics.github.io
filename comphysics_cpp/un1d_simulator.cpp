/*
Title       : Un1D - A Simple Uniform Motion Simulator
Description : This C++ program defines a class called Un1D that simulates the
              one-dimensional uniform motion of an object. It utilizes a constant
              velocity (vx) to compute the displacement from an initial position (x00)
              over time. The program calculates the number of simulation steps from
              the total simulation time and the time step (delt), and offers methods
              to compute the object's position at any time and to output (archive)
              the simulation parameters.
Compiler Notes:
    - Compiler: Any C++ compiler (e.g., g++ or clang++) supporting C++11 or later.
    - Compilation Example:
          g++ -std=c++11 -Wall -o un1d_simulator un1d_simulator.cpp
    - The program uses both C++ and C standard library headers, which are safely included.
*/

#include <iostream>     // For standard I/O stream operations.
#include <cstdlib>      // For general purpose functions (e.g., memory management).

// Definition of the Un1D class that simulates one-dimensional uniform motion.
class Un1D {
public:
    double x00;   // Initial position of the object.
    double delt;  // Time step size (delta time).
    double vx;    // Constant velocity of the object.
    double time;  // Total simulation time.
    int steps;    // Computed number of simulation steps, derived from time and delt.

    // Constructor:
    // Initializes the Un1D object with initial position, time step, constant velocity,
    // and total simulation time.
    // Parameters:
    //  x0    - Initial position.
    //  dt    - Time step size.
    //  vx0   - Constant velocity.
    //  ttot  - Total simulation time.
    Un1D(double x0, double dt, double vx0, double ttot)
        : x00(x0), delt(dt), vx(vx0), time(ttot) {
        // Calculate the number of simulation steps.
        steps = static_cast<int>(ttot / dt);
    }

    // Destructor:
    // Currently, no dynamic memory allocation is used. This function is here to show where
    // one would clean up resources if they were used.
    ~Un1D(void) {
        // Resource cleanup (if any) would occur here.
    }

    // Member function:
    // Computes the position x at a given time 'tt' using the uniform motion formula:
    // x = x0 + v * t.
    // Parameter:
    //  tt - Time at which the position is calculated.
    // Returns:
    //  The computed position at time 'tt'.
    double x(double tt) {
        return x00 + vx * tt;
    }

    // Member function:
    // Outputs (archives) the simulation parameters to the console.
    // It provides a snapshot of the initial conditions and computed steps.
    void archive() {
        std::cout << "x00: " << x00 << "\n";   // Display the initial position.
        std::cout << "delt: " << delt << "\n";   // Display the time step.
        std::cout << "vx: " << vx << "\n";       // Display the constant velocity.
        std::cout << "time: " << time << "\n";   // Display the total simulation time.
        std::cout << "steps: " << steps << "\n"; // Display the computed number of steps.
    }
};

int main() {
    // Create an instance of the Un1D class with:
    // Initial position (x0) = 0.0, time step (delt) = 0.1, constant velocity (vx) = 2.5,
    // Total simulation time = 10.0 seconds.
    Un1D sim(0.0, 0.1, 2.5, 10.0);

    // Display the computed position at time t = 5.0 seconds using the x() method.
    std::cout << "x at t=5: " << sim.x(5.0) << std::endl;

    // Display all simulation parameters using the archive() method.
    sim.archive();

    return 0;  // End of program.
}
