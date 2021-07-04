'''
question6.py


Write a script that generate a plot with the following characteristics:

        * Read the CSV file london_merged into a numpy array (hint: the
          delimiter in the file is ',').
        * Make a scatter plot where the data is the first column of the
        file data.csv.
        * Set the x values to be the row number of the csv (x=[0, 1, ...
        through the last row in the file).
        * Limit the x-axes of the plot to be from 0 to the number of rows.
        * Limit the y-axes of the plot to be from 0 to 6000.


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
from matplotlib import pyplot as plt

#Importing data into a Numpy array
DATA = np.genfromtxt('csv/data.csv', delimiter=',')

#Selecting the first column of data
Y_VALUES = DATA[:, 0]
#Finding the number of rows
NUM_ROWS = DATA.shape[0]
#x-axis will plot the row number from 1 to the row number
X_VALUES = range(1, NUM_ROWS+1)

#Plotting a scatter graph
plt.scatter(X_VALUES, Y_VALUES)
#Limiting the graph size
plt.xlim(0, NUM_ROWS)
plt.ylim(0, 6000)
#Displaying the graph
plt.show()
