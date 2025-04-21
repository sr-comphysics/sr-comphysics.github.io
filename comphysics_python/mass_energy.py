# Einstein's Mass-Energy Equivalence Calculator
# Import necessary libraries
import scipy.constants as sc  # Import physical constants from SciPy

# Print introductory information about the mass-energy equivalence
print("Einstein's Mass-Energy equivalence\n")
print("E - Energy\nm - Mass\nc - Velocity of light")

# Get the speed of light from SciPy constants
c = sc.speed_of_light  # Speed of light in meters per second
c_2 = c * c  # Calculate the square of the speed of light

# Start an infinite loop for user interaction
while True:
    # Display options for the user
    print("1. To Calculate Energy")
    print("2. To Calculate Mass")
    print("3. To Exit")
    
    # Get user input
    inp = input(">> ")
    
    # If the user chooses to calculate energy
    if inp == "1":
        mass = float(input("m = "))  # Get mass input from the user
        print("E = ", mass * c_2)  # Calculate and print energy using E = mc^2
    
    # If the user chooses to calculate mass
    elif inp == "2":
        energy = float(input("E = "))  # Get energy input from the user
        print("m = ", energy / c_2)  # Calculate and print mass using m = E/c^2
    
    # If the user chooses to exit the program
    elif inp == "3":
        break  # Exit the loop and end the program
    
    # If the user input is invalid
    else:
        print("Try again")  # Prompt the user to try again
