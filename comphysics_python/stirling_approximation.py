# Stirling's Approximation

# Importing Libraries
import matplotlib.pyplot as plt
import math as m

# Starting the loop with the specified range, hence "for loop".
for n in range(5, 21):
    v1 = m.log(m.factorial(n)) # Calculating [log(n!)]
    v2 = n*m.log(n) - n # Calculating [nlog(n) -n]
    # Print the calculated value
    print("For n =%3d: ln(n!) = %4.1f, nln(n)-n = %4.1f"%(n,v1,v2))
    pd = (v1-v2)/v1*100 # Calculating percentage difference
    # Scatter plotting 'n' against the 'percentage difference'
    plt.scatter(n,pd,color='black')
plt.ylabel('Percentage Difference')
plt.xlabel('n')
plt.title("Stirling's Approximation")
""" To save the graph in your local folder, just use the below mentioned function 
plt.savefig('stirling_approximation.png') """
plt.show()