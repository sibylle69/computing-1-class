'''
question3.py

Fix the errors so that this code runs when called
from the test file and passes all tests.

TOTAL POINTS AVAILABLE: 10 


Code Functionality (10)
10 points - no errors remain and code runs
-2 points for each remaining error or new ones introduced
0 points - all original errors remain 
'''


class Resistor:
    '''Resistor class representing 4 or 5 band resistors.'''
    resist_colours = {'black': 0,
                   'brown': 1,
                   'red': 2,
                   'orange': 3,
                   'yellow': 4,
                   'green': 5,
                   'blue': 6,
                   'violet': 7,
                   'grey': 8,
                   'white': 9, 
                   'silver': 0.1,
                   'gold':0.01}
    
    tol_colours = {'brown': 0.01,
                    'red': 0.02,
                    'green': 0.005,
                    'blue': 0.0025,
                    'violet': 0.001,
                    'grey': 0.0005,
                    'gold': 0.05,
                    'silver': 0.1}
    
    
    def __init__(self, band1, band2, band3, band4, band5=None):
        '''Creates a 4 or 5 band resistor with the input coloured bands.'''
        # check if input colours are valid values
        # raise ValueError if not
        if band1 not in self.resist_colours.keys():
            raise ValueError(band1 + ' not valid colour for band 1')
        if band2 not in self.resist_colours.keys():
            raise ValueError(band2 + ' not valid colour for band 2')
        if band3 not in self.resist_colours.keys():
            raise ValueError(band3 + ' not valid colour for band 3')
        # 4 band resistor
        if band5 is None:
            if band4 not in self.tol_colours.keys():
                raise ValueError(band4 + ' not valid colour for tolerance band')
        # 5 band resistor
        else:
            if band4 not in self.resist_colours.keys():
                raise ValueError(band4 + ' not valid colour for band 4')
            if band5 not in self.tol_colours.keys():
                raise ValueError(band5 + ' not valid colour for tolerance band')
        
        # set values
        self.b1 = band1
        self.b2 = band2
        self.b3 = band3
        # 4 band resistor 
        if band5 is None:
            self.tolerance = band4
            self.num_bands = 4
        # 5 band resistor
        else:
            self.b4 = band4
            self.tolerance = band5
            self.num_bands = 5

    def get_value(self):
        '''Returns the calculated value of the resistor in Ohms.'''       
        # 4-band value = <band1 band2> (each a digit) x 10^band3
        if self.num_bands == 4:
            value = (Resistor.resist_colours[self.b1] * 10 + Resistor.resist_colours[self.b2]) * 10**Resistor.resist_colours[self.b3]
        
        # 5-band value = <band1 band2 band3> (each a digit) x 10^band4
        if self.num_bands == 5:
            value = (Resistor.resist_colours[self.b1] * 100 + Resistor.resist_colours[self.b2] * 10 + Resistor.resist_colours[self.b3]) * 10**Resistor.resist_colours[self.b4]
       
        return value
    
    def get_min_value(self):
        '''Return the minimum value within the tolerance of the resistor value.'''
        # Calculate target value of resistor
        target = self.get_value()
        # Return target value - (% tolerance * target value)
        return target - (target * Resistor.tol_colours[self.tolerance])     
    
    def get_max_value(self):
        '''Return the maximium value within the tolerance of the resistor value.'''
        # Calculate target value of resistor
        target = self.get_value()
        # Return target value - (% tolerance * target value)
        return target + (target * Resistor.tol_colours[self.tolerance])  
    
    def parallel_add(self, second_resistor):
        '''Implements the parallel addition of two resistors.'''
        # 1/R_total = 1/R_1 + 1/R_2
        return 1./(1./self.get_value() + 1./second_resistor.get_value())

    def __add__(self, second_resistor):
        '''Overriding the built-in to implement series addition of two resistors.'''
        # R_total = R_1 + R_2
        return self.get_value() + second_resistor.get_value()
