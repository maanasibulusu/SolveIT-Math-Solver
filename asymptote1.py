#http://www.cs.cmu.edu/~112/schedule.html
def almostEqual(d1, d2, epsilon=10**-5):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1)) < epsilon

#from  derivative_withbase import *
from numpy import linspace, sin, cos, tan,exp
import math
#from derivative_withbase import *
from derviative_integral import *

class Asymptote :
    def __init__(self, object ):
        self._function = object

    #xn+1 = xn - f(x)/f'(x)
    def __call__(self, x0):
       pass

    def __str__(self):
        return str(range_list)
    
    def evaluate (self, expr, x):
        pass

    def HorAsymptote(self):
        if (isinstance (self._function, Element)):
            return self.HorAsymptoteElement(self._function)
        if (isinstance (self._function, Series)):
            return self.HorAsymptoteSeries(self._function)
                    
    def HorAsymptoteElement(self,element): 
        #print('HorAsymptoteElement :', str(element), type(element))

        if (isinstance(element, Element) != True ):
            return ('No Horizontal Asymptote')

        if(element._exp >=1 ):
            if (isinstance (element, Element) ):
                return ('No Horizontal Asymptote')
        elif(element._exp < 1 ):
            if (type(element) == power or type(element) == Basic):
                base = element._base
                if(type(base) == power or type(base) == Basic or base == None):
                    return ('Horizontal Asymptote at y=0')
                else :
                    return ('No Horizontal Asymptote')

    def HorAsymptoteSeries(self,series): 
        #print('HorAsymptoteSeries :', str(series))

        if (isinstance(series, Series ) != True ):
            return ('No Horizontal Asymptote')

        elements = series._elements

        #Check if the series is polinomial 
        maxExp,maxCoff = 0, 1
        maxExpN,maxCoffN = 0, 1
        computeN = False
      
        for elem in elements: 
            #print('HorAsymptoteSeries :', str(elem), type(elem))

            if( type(elem) == str):
                if(elem == '-' or elem == '+'):
                    continue
                elif (elem.strip() == '*'):
                    return ('No Horizontal Asymptote')
                elif (elem.strip() == '/'):
                    computeN = True
                    continue
            
            if(type(elem) == power or type(elem) == Basic):
                if (computeN == False):
                    maxExp = max(maxExp,elem._exp)
                    maxCoff = max(maxCoff,elem._coffecient)
                else:

                    maxExpN = max(maxExpN,elem._exp)
                    maxCoffN = max(maxCoffN,elem._coffecient)
            else :
                return ('No Horizontal Asymptote')
        if(maxExp >=1  and maxExpN >=1  ):
            if(maxExp/maxExpN  == 1):
                return maxCoffN/maxCoff
            elif (maxExp/maxExpN  > 1):
                return ('No Horizontal Asymptote')
            elif (maxExp/maxExpN  < 1 ):
                return ('Horizontal Asymptote at y=0')
            
        return ('No Horizontal Asymptote')
''' 
x = Basic('x')

y = 1/x
r = Asymtote (y) 
print(r.HorAsymptote())

y = x**2 -2*x +2 
r = Asymtote (y) 
print(r.HorAsymptote())

y = (x-1)/(x-2) 
r = Asymtote (y) 
print(r.HorAsymptote())
'''