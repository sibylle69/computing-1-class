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
    def __init__(self, milk = True, sugar = 0):
    # set the instance attributes milk and sugar with 
    # the passed in values
        self.milk = milk
        self.sugar = sugar


    # write a methods that adds 1 sugar to the sugar instance 
    # attribute each time it is called
    def more_sugar(self):
        self.sugar += 1
        return self.sugar

    # write a methods that adds milk only if there wasn't milk before
    # (the milk instance attribute was False). If milk was already True
    # then raise a ValueError.
    def add_milk(self):
        if self.milk:
            raise ValueError
        else:
            self.milk = True
        return self.milk

    # write a method that allows __str__ to be called on the Cuppa 
    # instance which returns the following strings:
    #  if milk and no sugar: 'Just milk, please'
    #  if milk and sugar > 1: 'Milk and N sugars, please'
    #  if milk and 1 sugar: Milk and 1 sugar, please'
    #  if no milk and sugar > 1: 'Black and N sugars, please'
    #  if no milk and 1 sugar 1: 'Black and 1 sugar, please'
    #  if no milk and no sugar: 'Just black, please'
    def __str__(self):
        return self.test_for_sugar()

    def test_for_sugar(self):
        if self.sugar >1:
            return self.test_for_milk() + " and " + str(self.sugar) + " sugars, please"
        elif self.sugar != 0:
            return self.test_for_milk() + " and " + str(self.sugar) + " sugar, please"
        else:
            return "Just " + self.test_for_milk().lower() + ", please"

    def test_for_milk(self):
        if self.milk == True:
            return "Milk"
        else:
            return "Black"


