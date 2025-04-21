/*
Title       : UmMotion Simulator: 1D and 2D Uniform Motion in C++
Description : This C++ program demonstrates uniform motion simulation using
              object-oriented techniques. It defines a base class, Um1D, to model
              one-dimensional uniform motion and a derived class, Um2D, to extend
              the simulation into two dimensions. The simulation calculates the
              final positions using the formulas:
                  x(t) = x00 + vx*t,
                  y(t) = y00 + vy*t.
              Each class provides an archive() function to output internal state data.
Compiler Notes:
    - Requirements: A C++ compiler supporting C++11 or later (e.g., g++ or clang++).
    - Compilation Example:
          g++ -std=c++11 -Wall -o um_motion_simulator um_motion_simulator.cpp
*/

#include <iostream> // For standard input/output

// Base class: represents one-dimensional (x) uniform motion.
class Um1D {
public:
    double x00;   // Initial x position.
    double delt;  // Time step interval.
    double vx;    // Constant velocity in x direction.
    double time;  // Total simulation time.
    int steps;    // Number of simulation steps, computed from total time / time interval.

    // Constructor:
    // Initializes the Um1D object with initial x position, time step interval,
    // constant velocity, and total simulation time. It computes the number of steps.
    // Parameters:
    //   x0    - Initial x position.
    //   dt    - Time interval (delta t).
    //   vx0   - Constant velocity along x.
    //   ttot  - Total simulation time.
    Um1D(double x0, double dt, double vx0, double ttot)
        : x00(x0), delt(dt), vx(vx0), time(ttot)
    {
        // Calculate the number of steps (integer division of total time by time step).
        steps = static_cast<int>(ttot / dt);
    }

    // Virtual destructor for safe polymorphic cleanup.
    virtual ~Um1D(void) {
        std::cout << "Class Um1D destroyed" << std::endl;
    }

    // Member function:
    // Calculates the x position at a given time 'tt' based on the constant velocity formula.
    // Parameter:
    //   tt - The time at which to evaluate the position.
    // Returns:
    //   The computed x position.
    double x(double tt) {
        return x00 + tt * vx;
    }

    // Archive function:
    // Prints the internal class member values to std::cout.
    // Declared virtual to allow overriding in derived classes.
    virtual void archive() {
        std::cout << "x00: " << x00 << "\n"
                  << "delt: " << delt << "\n"
                  << "vx: " << vx << "\n"
                  << "time: " << time << "\n"
                  << "steps: " << steps << "\n";
    }
};

// Derived class: represents two-dimensional (x and y) uniform motion.
class Um2D : public Um1D {
public:
    double y00; // Initial y position.
    double vy;  // Constant velocity in y direction.

    // Constructor:
    // Initializes the derived Um2D object by calling the base class constructor
    // for x motion and initializing y-specific members.
    // Parameters:
    //   x0    - Initial x position.
    //   dt    - Time step interval.
    //   vx0   - Constant velocity in x direction.
    //   ttot  - Total simulation time.
    //   y0    - Initial y position.
    //   vy0   - Constant velocity in y direction.
    Um2D(double x0, double dt, double vx0, double ttot, double y0, double vy0)
        : Um1D(x0, dt, vx0, ttot), y00(y0), vy(vy0)
    {
    }

    // Override destructor for the derived class.
    ~Um2D(void) override {
        std::cout << "Class Um2D destroyed" << std::endl;
    }

    // Member function:
    // Calculates the y position at a given time 'tt' using the uniform motion formula.
    // Parameter:
    //   tt - The time at which to evaluate the y position.
    // Returns:
    //   The computed y position.
    double y(double tt) {
        return y00 + tt * vy;
    }

    // Archive function:
    // Overrides the base class archive() function to print both base and derived data.
    void archive() override {
        // Output the archived data from the base class.
        Um1D::archive();
        // Output the additional data for y motion.
        std::cout << "y00: " << y00 << "\n"
                  << "vy: "  << vy << "\n";
    }
};

int main() {
    // Create an instance of Um2D with the following initial conditions:
    // x0 = 0.0, dt = 0.1 seconds, vx = 2.5 m/s, total time = 10.0 seconds,
    // y0 = 0.0, vy = 1.5 m/s.
    Um2D sim(0.0, 0.1, 2.5, 10.0, 0.0, 1.5);

    // Define a sample time for position calculation.
    double t_sample = 5.0;

    // Output the positions at time t_sample.
    std::cout << "At t = " << t_sample << " sec:" << std::endl;
    std::cout << "x = " << sim.x(t_sample) << std::endl;  // Compute and display x position.
    std::cout << "y = " << sim.y(t_sample) << std::endl;  // Compute and display y position.

    // Archive and display all internal state information of the simulation.
    sim.archive();

    return 0;  // End of program.
}
