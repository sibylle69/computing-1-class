'''
question5.py

Write a script that generate a plot with the following characteristics:

    * Plot the line y = 3x^2 -10x + 30
    * The x-axis values of the plot should be 100 from -10 to 10.
    * Make sure the line is green and 3 points thick.
    * Turn the grid on (can leave at default spacing, ok if different from image).


TOTAL POINTS AVAILABLE: 10 


Code Functionality (7)
7 points - desired plot is generated and code is efficient and Pythonic

5-6 points - desired plot is generated, but code could be significantly 
improved to be more Pythonic

3-4 points - plot has some errors

1-2 points - no plot is generated, but some effort was made to generate one

0 points - no effort made to answer question



Code Readability (3)
3 points - Well commented, clear code 

1-2 points - Some issues related to comments or issues such as variable 
names could be improved 

0 points - multiple and repeated significant style issues, code very 
difficult to understand

'''

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

x = np.linspace(-10,10, 100)
y = 3*x**2 -10*x + 30

plt.title('Question 5 Plot')
plt.grid()
plt.xlim(-10,10)
plt.xticks(np.linspace(-10,10, 5))
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.plot(x,y, '-g', linewidth = 3)
plt.show()