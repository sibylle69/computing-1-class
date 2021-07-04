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

from numpy import arange
import matplotlib.pyplot as plt

#Creating empty list
X_LIST = []
for i in arange(-10., 10.2, 20/100):
    X_LIST.append(i)
#Filling list with range of floats between -10 and 10.2 (exclusive)
#With a gap of 20/100 so that there will be 100 points plotted

#Creating empty list
Y_LIST = []
for x in X_LIST:
    y = 3*(x**2) - 10*x + 30
    Y_LIST.append(y)
#Filling list with y values which correspond to x values via the equation

#Plotting the x and y values on a graph with green set as the colour and a width of 3
plt.plot(X_LIST, Y_LIST, color='g', linewidth=3)
#Turning on the graph grid
plt.grid(True)
#Labelling the x and y axis and giving the graph a title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Question 5 Plot')
#Displaying the graph
plt.show()
