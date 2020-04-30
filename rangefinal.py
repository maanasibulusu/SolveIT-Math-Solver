#http://www.cs.cmu.edu/~112/schedule.html
def almostEqual(d1, d2, epsilon=10**-5):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1)) < epsilon

#from  derivative_withbase import *
from numpy import linspace, sin, cos, tan,exp
import math
from derviative_integral import *

class Limit:
    def __init__(self,lower = None,upper = None ,oper=""):
        self._lower = lower
        self._upper = upper
        self._oper = oper
    def __str__(self):
        limit = ""
        if (self._lower != None ):
            limit += (str(self._lower) + " ")
        if (self._oper != "" ):
            limit += (str(self._oper) + " ")
        if (self._upper != "" ):
            limit += (str(self._upper) + " ")
        if('inf' in limit):
            limit = limit.replace('inf','Infinity')
        return limit
    
class RangeTesting :
    def __init__(self, object ):
        self._function = object
        self._limits = []
    def add(self, limit):
        self._limits.append(limit)

    def removeAll(self):
        self._limits.clear()
    
    #xn+1 = xn - f(x)/f'(x)
    def __call__(self, x0):
       pass

    def __str__(self):
        range_list = []
        for  elem in self._limits:
            range_list.append(str(elem))
        return str(range_list)
    
    def evaluate (self, expr, x):
        pass

    def rangeF(self):
        if (isinstance (self._function, Element)):
            return self.rangeElement(self._function)
        if (isinstance (self._function, Series)):
            return self.rangeSeries(self._function)
        

    def isFractionSqrt(exp):
        (numer, denom) = float(exp).as_integer_ratio()
        while (denom > 1 ):
            if(denom  % 2 == 0):
                denom //= 2
            else:
                return False
        return True
        

    def rangeSeries(self, series):
        #Range of series or composite function is range of all the elements
        rangeSeries = ""
        for elem in  series._elements :
            if(isinstance(elem,Element)):
                rangeSeries += self.rangeElement(elem)

        limitS = Limit()
        for limit in self._limits:
            if (limitS._lower == None):
                limitS._lower = limit._lower
            else :
                if(limitS._lower != None and limit._lower != None):
                    limitS._lower = min(limitS._lower,limit._lower)

            limitS._oper = 'to'

            if (limitS._upper == None):
                limitS._upper = limit._upper
            else :
                if(limitS._upper != None and limit._upper != None):
                    limitS._upper = max(limitS._upper,limit._upper)       
        self.removeAll()
        self.add(limitS)
        return str(self)
                
    def rangeElement(self,element): 
        #print('Range :', str(element))
        if(element._exp >=1 ):
            if (type(self) == ln ):
                (lower, oper, upper) = (-math.inf, 'to', math.inf) 
                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('-Infinity to +infinity ')
            elif (type(element) == power or type(element) == Basic):
                base = element._base
                if(base == None or type(base)== Basic or type(base)==power):
                    (lower, oper, upper) = (-math.inf, 'to', math.inf)
                else :return self.rangeElement(base)

                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('-Infinity to +infinity ')
            elif (type(element) == exp ):
                (lower,oper, upper) = (1,'to', math.inf) 
                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('0 to +infinity ')
            elif (type(element) == sin or type(element) == cos):
                (lower,oper, upper) = (-1,'to', 1)
                if element._constant != 0 :
                    lower += element._constant
                    upper += element._constant
                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('%f to %f'%(-value,value))
            elif (type(element) == tan ):
                (lower, oper, upper) = (-math.inf, 'to', math.inf) 
                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('-Infinity to +infinity ')
            elif (type(element) == sec ):
                (lower, oper, upper) = (-math.inf, 'to', -1) 
                limit = Limit(lower,upper,oper)
                self.add(limit)
                (lower, oper, upper) = (1, 'to', math.inf) 
                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('[-Infinity to -1],[1 to +infinity]')
            else:
                (lower, oper, upper) = (-math.inf, 'to', math.inf) 
                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('-Infinity to +infinity ')
        elif(element._exp > 0 and element._exp  < 1 ):
            if (type(self) == ln ):
                (lower, oper, upper) = ( 0, 'to', math.inf) 
                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('-Infinity to +infinity ')
            elif (type(element) == power or type(element) == Basic):
                base = element._base
                if(base == None or type(base)== Basic or type(base)==power):
                    (lower, oper, upper) = (0, 'to', math.inf)
                    limit = Limit(lower,upper,oper)
                    self.add(limit)
                elif(type(base) == sin or type(base) == cos):
                    (lower, oper, upper) = (0, 'to', 1)
                    if element._constant != 0 :
                        lower += element._constant
                        upper += element._constant
                    limit = Limit(lower,upper,oper)
                    self.add(limit)
                elif (type(base) == exp ):
                    (lower,oper, upper) = (1,'to', math.inf) 
                    limit = Limit(lower,upper,oper)
                    self.add(limit)
                elif (type(element) == tan ):
                    (lower, oper, upper) = (0, 'to', math.inf) 
                    limit = Limit(lower,upper,oper)
                    self.add(limit)
                    #range_ll.append('-Infinity to +infinity ')
            elif (type(element) == sec ):
                    (lower, oper, upper) = (1, 'to', math.inf) 
                    limit = Limit(lower,upper,oper)
                    self.add(limit)
                #range_ll.append('-Infinity to +infinity ')
            elif (type(element) == exp ):
                (lower,oper, upper) = (1,'to', math.inf) 
                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('0 to +infinity ')
            elif (type(element) == sin or type(element) == cos):
                (lower, oper, upper) = (0, 'to', 1)
                if element._constant != 0 :
                    lower += element._constant
                    upper += element._constant
                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('%f to %f'%(-value,value))
            elif (type(element) == tan ):
                (lower, oper, upper) = (0, 'to', math.inf) 
                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('-Infinity to +infinity ')
            elif (type(element) == sec ):
                (lower, oper, upper) = (1, 'to', math.inf) 
                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('[-Infinity to -1],[1 to +infinity]')
            else:
                (lower, oper, upper) = (0, 'to', math.inf) 
                limit = Limit(lower,upper,oper)
                self.add(limit)
                #range_ll.append('-Infinity to +infinity ')
        else :
            #Evaluate the denominator 
            # Needs special cases for sqrt, cube root

            (lower, oper, upper) = (1, 'to', math.inf) 
            limit = Limit(lower,upper,oper)
            self.add(limit)
            #range_ll.append('1 to +infinity ')
        return str(self)

'''
x = Basic('x')

y = 2*x -1
r = RangeTesting(y)
print(r.rangeF())

y = 2*x**2 -1
r = RangeTesting(y)
print(r.rangeF())

y = sin(x)+ 2
print(y, RangeTesting(y).rangeF())

y = sin(2*x-1)**2
print(y, type(y),RangeTesting(y).rangeF())

y = 1/x**2
print(y, RangeTesting(y).rangeF())

y = ln(x)
print(y, RangeTesting(y).rangeF())

y = cos(x)**0.5
print(y, RangeTesting(y).rangeF())

y = exp(x)**0.5
print(y, RangeTesting(y).rangeF())

y = (exp(x)**-1)
print(y, RangeTesting(y).rangeF())


y = ln(x) **0.5
print(y, RangeTesting(y).rangeF())

y = sec(x)
print(y,type(y), RangeTesting(y).rangeF())

y = x * sin(x)
print(y, RangeTesting(y).rangeF())

'''