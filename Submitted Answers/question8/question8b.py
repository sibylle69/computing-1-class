'''
question8.py



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
import random

class ImperialStudent():
    '''Base class of students at Imperial.'''
    # Create a constructor that takes the surname of a student as the
    # only argument. It then sets the following instance attributes:
    #  - surname (string)
    #  - cid (random int between 10000 and 99999)
    #  - on_loan (empty dictionary)
    def __init__(self, surname):
        self.surname = surname
        self.cid = random.randint(10000, 99999)
        self.on_loan = {}

    # Created a method called check_out() that takes two arguments:
    #  - item_description (string)
    #  - due date (int in YYYYMMDD format)
    # the method adds the item and due date to the on_loan dictionary
    # with the item_description as the key and the due date as the value
    def libary_check_out(self, item_description, due_date):
        self.on_loan[item_description] = due_date
    

    # create a method called get_next_due() that will 
    # return the next item_description due in the instance attribute
    # on_loan. You do not need to worry about the current date or
    # past due items. Just return the item with the earliest date.
    def get_next_due(self):
        return min(self.on_loan, key=self.on_loan.get)



# Create a class called DEStudent that inherits from ImperialStudents
class DEStudent(ImperialStudent):

    # Add a class attribute of faculty which is set 
    # to 'Engineering' by default 
    faculty = "Engineering"

    # Create a constructor that takes the surname and also the year. 
    # It adds the instance attribute of the year and otherwise inherits the
    # constructor of the base class
    def __init__(self, surname, year):
        super().__init__(surname)
        self.year = year

    # Add a method that lends tools from the ACE Workshop
    # called ace_hammer_check_out which takes the due_date as the only 
    # input argument (same YYYYMMDD format as above).
    # It then checks out the item_description 'hammer' with the 
    # input due_date using the base class's library_check_out() method.
    def ace_hammer_check_out(self, due_date):
        self.libary_check_out("hammer", due_date)