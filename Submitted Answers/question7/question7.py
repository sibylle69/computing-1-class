'''
question7.py

TOTAL POINTS AVAILABLE: 30 

Code Functionality (5 points per method, 20 across whole class)
5 points - all tests pass and code is efficient and Pythonic

3-4 points - all tests pass, but code could be significantly 
improved to be more Pythonic

2 points - at least one test fails, but much of code does work and 
rest would work with small changes

1 point - no test passes and effort has been made to answer question 
but would need significant changes/additions to make any of the code 
function correctly

0 points - no effort made to answer question


Code Readability (10 across whole class)
10 points - Well commented, clear code where PyLint returns no or 
few errors (error related to removing else/elif can be ignored)

6-9 points - Most of the code is using good practice with comments, docstrings
and names, but there is room for improvement

1-5 points - Many issues related to problems such as dense, unexplained lines
of code and variable names could be improved 

0 points - multiple and repeated significant style issues, code very 
difficult to understand
'''


class Cuppa():
    # constructor
    # has 2 keyword arguments:
    #    - milk (boolean, default True)
    #    - sugar (number of teaspoons, default 0)
    # set the instance attributes milk and sugar with 
    # the passed in values

    def __init__(self, milk = True, sugar = 0): 
        self.milk = milk
        self.sugar = sugar

    # write a method that adds 1 sugar to the sugar instance 
    # attribute each time it is called
    def more_sugar(self): 
        self.sugar += 1
        return self.sugar

    # write a method that adds milk only if there wasn't milk before
    # (the milk instance attribute was False). If milk was already True
    # then raise a ValueError.
    def add_milk(self): 
        if self.milk == False: 
            self.milk = True
            return self.milk
    
        raise ValueError 

    # write a method that allows __str__ to be called on the Cuppa 
    # instance which returns the following strings:
    #  if milk and no sugar: 'Just milk, please'
    #  if milk and sugar > 1: 'Milk and N sugars, please'
    #  if milk and 1 sugar: Milk and 1 sugar, please'
    #  if no milk and sugar > 1: 'Black and N sugars, please'
    #  if no milk and 1 sugar 1: 'Black and 1 sugar, please'
    #  if no milk and no sugar: 'Just black, please'

    def __str__(self): 
        if self.milk == True: 
            if self.sugar == 0: 
               return 'Just milk, please' 
            elif self.sugar > 1: 
                return f'Milk and {self.sugar} sugars, please'
            elif self.sugar == 1: 
                return 'Milk and 1 sugar, please'
     
        else: 
            if self.sugar > 1: 
                return f'Black and {self.sugar} sugars, please'
            elif self.sugar == 1: 
                return 'Black and 1 sugar, please'
            else:
                return 'Just black, please'