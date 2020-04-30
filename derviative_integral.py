enum_oper  = { '__add__': '+',
               '__sub__':'-',
               '__mul__':'*',
               '__pow__': '**',
               '__truediv__': '/',
               '__perr__':')',
               '__perl__':'('
            }
def oper(p):
    return(str(enum_oper[p]))
enum_integ_priority = {'inv':  5,
                       'ln' :  4,
                       'basic':3,
                       'power':3,
                       'sin'  :2,
                       'cos'  :2,
                       'tan'  :2,
                       'sec'  :2,
                       'exp'  :1
                      }
def integ_prio(p):
    return (enum_integ_priority[p])
#http://www.cs.cmu.edu/~112/schedule.html
def almostEqual(d1, d2, epsilon=10**-5):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1)) < epsilon
#Class Negator is Borrowed from
#https://stackoverflow.com/questions/14247373/python-none-comparison-should-i-use-is-or
class Negator(object):
    def __eq__(self,other):
        return not other
import math
from numpy import linspace
def rootsF ( function , d_min =-10 , d_max =10 , no_iter = 10001):
    #find Domain
    #domainV = domain(function)
    if (d_min ==0 ) :d_min =  -10
    if (d_max ==0 ) :d_min =  10
    if (no_iter ==0 ) :no_iter =  1001
 
    #Interpret  domainV
    x = linspace(d_min, d_max, no_iter)
    g = function(x)
    roots = []
    for elem in  range(len(g)):
        if almostEqual(round(g[elem]),0): roots.append(x[elem])
    roots_set = set()
    for i in range(len(roots)):
        roots_set.add(round(roots[i],1))
    return (list(roots_set))

class ErrorCodes:
    error = {101: 'Could not find derivative',
             102: 'Could not integration',
             104: 'Could not find domain',
             105: 'Could not find range',
             106: 'Could not find Asymptote',
             107: 'Custom Message'
            }
    def __init__(self, code, reason = '' ):
        _code = code
        _reason = reason
   
#Class Basic Elment
class Element:
    #Constructor , Object variables
    def  __init__(self):
       self._name = ''
       self._coffecient = 1
       self._type = ''
       self._isdeferentiable = True
       self._isContinuos = True
       self._base = None
       self._exp = 0
       self._basic=None
       self._constant = 0
       self._operand = ''
    def toString(self, brackets = True):
        base = ""
        none = Negator()
        if none == self._base  :
            base = ("(%s)" %self._name)
        else:
            coff1 , exp1, oper1,constant1 = ("","","","")
            coff1 = str(self._base._coffecient)
            if(self._base._exp ==  1): exp1  = ""
            else:    exp1 = str(self._base._exp)
            if(self._base._exp !=  1): oper1 = str(self._base._operand)
            if(self._base._constant > 0): constant1 = "+" + str(self._base._constant)
            if(self._base._constant < 0): constant1 =  str(self._base._constant)
            primitive = str(self._base)
            #Ex: (2*x+1)**2
            if brackets == True:
                base = ("(%s)" %str(self._base) )
            else:
                base = ("%s" %str(self._base) )
            #("(%s*%s%s)%s%s" %(coff1,primitive,constant1,oper1,exp1))
       
        coff , coff1,exp1, oper,constant = ("","","","","")
        #coff = str(self._coffecient)
        if(type(self._coffecient) == Constant):
            coff = self._coffecient._constant
        else: coff = self._coffecient
        if(coff == 1): coff1 == ""
        elif(coff == -1 ): coff1 = "-".format(round(coff, 1))
        else: coff1 = "{:.2f}*".format(round(coff, 1))
        if(self._exp ==  1): exp2  = ""
        else:    exp2 = str(self._exp)
        if(self._exp !=  1): oper = str(self._operand)
        if(self._constant > 0): constant = "+" + str(self._constant)
        if(self._constant < 0): constant =  str(self._constant)
        if(type(self) in (Basic,power) ):
            #y = 2*(2x+1)**3 + 4
            self._basic= ("%s%s%s%s%s" %(coff1,base,oper,exp2,constant))
        elif(type(self) in (sin, cos ,tan,sec, ln)):
            self._basic= ("%s%s%s%s" %(coff1,self._name,base,constant))
        elif(type(self)  == exp ):
            self._basic = ("%s%s%s%s" %(coff1,self._name,base,constant))
        return self._basic
    #print the class representation
    def __str__(self):
       return self.toString()
    def __repr__(self):
        return self.toString()
    def __eq__(self,other):
        #consider power an basic element are are same type for mult and div
        return (type(self) == type(other)  and \
            (self._type == other._type ) and \
            self._base == other._base)
    def kindOf(self,other):
        #print('kindOf = ', type(self), type(other))
        sameType = False
        sameTypeList = ('power','basic')
        if (isinstance(self,Element) and isinstance(other,Element)):
            #print('kindOf2  self = ', self.__dict__)
            #print('kindOf2 other = ', other.__dict__)
            if (self._type in sameTypeList and  other._type in sameTypeList):
                sameType = True
            if((sameType == True or self._type == other._type ) \
                    and self._base == other._base \
                    and self._exp == other._exp):
                    #print('kindOf2 return = ',True )
                    return True
        return False
    def __add__(self,other):
        #Add or subtract all constanst
        #If is same object add them up
        if(type(other) == int or type(other) == float or \
                    type(other)== Constant):
            if(type(other)== Constant):  other_c = other._constant
            else:  other_c = other
            constant = self._constant + other_c          
            pow = power(self._base,self._exp,self._coffecient , constant)
            return pow
        if(self.__eq__(other) == True and self._exp == other._exp):
            coff = self._coffecient  + other._coffecient
            pow = power(self._base, self._exp  ,coff, self._constant)
            return pow
       #If is different  objects create series
        series  = Series()
        series.add(self)
        series.add(oper('__add__'))
        series.add(other)
        return series
    def __radd__(self, other):
        return self.__add__(other)
    def __sub__(self,other):
        #Add or subtract all constanst
        #If is same object add them up
        if(type(other) == int or type(other) == float):
            constant = self._constant - other       
            pow = power(self._base,self._exp ,self._coffecient, constant)
            return pow
        if(self.__eq__(other) == True and self._exp == other._exp):
            coff = self._coffecient  - other._coffecient
            pow = power(self._base, self._exp, coff, self._constant)
            return pow
        series  = Series()
        series.add(self)
        series.add(oper('__sub__'))
        series.add(other)
        return series
    def __rsub__(self, other):
        return self.__sub__(other)
   
    def __pow__(self, other):
        #(ka^m )** n = k^n * a^mn
        #print('Iama in __POW__', type(self),type(other),other,self.__dict__)
        if(other ==0):   #x^0 = 1
            #return a constant object
            const = Constant(self._coffecient )
            return const
        if (self._constant == 0 ):
            exp = self._exp * other
            coff = self._coffecient ** other
            return power(self._base,exp,coff)
        #Ex y = 2*(2x+1)^3
        else :
            #Create a new base
            #re-adjust the base
            #exp = self._exp * other
            exp =  other
            coff = 1
            constant = 0
            return power(self,exp,coff,constant)
    #def __rpow__(self, other):
    #    return self.__pow__(other)
   
    def __mul__(self, other):
        #If multiply with constant
        #If 5X ^2 ** 2= 10x^2
        #5X ^2 * x^4= 5x^6
        #5sin(x) * 6sin(x)
        #5sin(x) * 6cos(x)
        #(e^x+1)*(e^x+6)
        #Always create
        if(type(other) == int or type(other) == float or \
                    type(other)== Constant):
            if(type(other)== Constant):  other_c = other._constant
            else:  other_c = other
            #Multiply the _coffecient with other Ex: y = 2x
            pow = power(self._base,self._exp ,self._coffecient * other_c)
            return pow
        #if it is same object and constants are same
        # Ex: y = 2x * 4x = 8 x^2
        #Ex: y = (2x+1)(4x+1) should be treated like different objects
        if(self.__eq__(other) == True and self._constant == 0 and \
                      other._constant == 0 ):
            exp = self._exp + other._exp
            coff = self._coffecient * other._coffecient        
            pow = power(self._base,exp,coff)
            return pow
        #If is different  objects create series
       
        series  = Series()
        series.add(self)
        series.add(oper('__mul__'))
        series.add(other)
        return series
       
    def __rmul__(self, other):
        return self.__mul__(other)
    def __truediv__(self, other):
        #If multiply with constant
        #If 5X ^2 / 2= 10x^2
        #5X ^2 / x^4= 5x^6
        #5sin(x) / 6sin(x)
        #5sin(x) / 6cos(x)
        #(e^x+1)/(e^x+6)
        if(type(other) == int or type(other) == float):
            #Multiply the _coffecient with other Ex: y = 2x
            pow = power(self._base,self._exp*-1 ,self._coffecient / other)
            return pow
        #if it is same object and constants are same
        # Ex: y = 2x / 4x = 8 x^2
        #Ex: y = (2x+1)/(4x+1) should be treated like different objects
        if(self.__eq__(other) == True and self._constant == 0 and \
                      other._constant == 0 ):
            exp = self._exp / other._exp
            coff = self._coffecient / other._coffecient        
            pow = power(self._base,exp,coff)
            return pow
        #If is different  objects create series
       
        series  = Series()
        series.add(self)
        series.add(oper('__truediv__'))
        series.add(other)
        return series
       
    def __rtruediv__(self, other):
        return self.__truediv__(other)
    def domain(self):
        domain_ll = []
        if (type(self) == ln ):
            base = self._base
            if base == None :
                value = 0
            else :
                value = (base._constant * -1 /base._coffecient)**(1/base._exp)
            domain_ll.append('x > ')
            domain_ll.append( value)
        else :
            domain_ll.append('All Real Numbers')
        return domain_ll
    # No derivative
    def derivative(self):
        pass
    def evaluate (self):
        pass
    def integrate (self, noBase = False):
        pass
    def simplify(self):
        return self
#Element which is the base element for all
class Constant(Element):
    def __init__(self,constant=0):
        super().__init__()
        self._name = ""
        self._type = 'constant'
        self._constant = constant
        self._operand = ""
        self._basic = str(self._constant)
    def __eq__(self, other):
        if (type(other) == Constant):
            return (other._constant == self._constant)
        elif (type(other) == int or type(other) == float):
            return (self._constant ==  other )
        else: return False
       
    def __str__(self):
        return str(self._constant)
    def __add__(self, other):
        if(type(other)== Constant or type(other) == int or \
                                        type(other)==float):
            if(type(other) == Constant ): constant_o = other._constant
            elif (type(other) == int or type(other) == float):
                constant_o= other
            return Constant(self._constant + constant_o )
    def __sub__(self, other):
        if(type(other)== Constant or type(other) == int or \
                                        type(other)==float):
            if(type(other) == Constant ): constant_o = other._constant
            elif (type(other) == int or type(other) == float):
                constant_o= other
            return Constant(self._constant - constant_o )
    def __mul__(self, other):
        if(type(other)== Constant or type(other) == int or \
                                        type(other)==float):
            if(type(other) == Constant ): constant_o = other._constant
            elif (type(other) == int or type(other) == float):
                constant_o= other
            return Constant(self._constant * constant_o )
    def __truediv__(self, other):
        if(type(other)== Constant or type(other) == int or \
                                        type(other)==float):
            if(type(other) == Constant ): constant_o = other._constant
            elif (type(other) == int or type(other) == float):
                constant_o= other
            return Constant(self._constant / constant_o )
    def derivative(self):
        const = Constant(0)
        return const
    def integrate (self):
        #Create another power object
        #Integral of constant = cx
        exp =  1  # X^(1+1)
        coff = self._constant
        const = 0
        base = Basic('x')
        #Create a seperate Power Object
        pow_c = power(base, exp, coff)
        return pow_c
class Basic(Element):
    def  __init__(self, name):
        super().__init__()
        self._name = name
        self._type = 'basic'
        self._exp = 1
        self._basic= name
   
    #  df/dx for x = 1
    def derivative(self):
        deriv_x = 1
        coff = deriv_x * self._coffecient
        #return a constant object
        const = Constant(coff)
        return const
   
    #Integration of ax = ax^2/2 + c *x if constant is present
    def integrate(self):
        exp = self._exp + 1  # X^(1+1)
        coff = self._coffecient *0.5
        const = self._constant
        #Create a seperate Power Object
        base = Basic(self._name)
        pow_x = power(base ,exp, coff)
        if (const == 0 ):
            return pow_x
        else :
            const = Constant(const)
            pow_c = const.integrate()
   
            #Create series
            series  = Series('integrate')
            series.add(pow_x)
            series.add(oper('__add__'))
            series.add(pow_c)
            return series
   
class exp(Element):
   
    def  __init__(self, base, coff = 1, constant = 0):
        #if (isinstance(base,Element) != True and type(base) != None):
        #   raise TypeError("input must be a Element or None ")
        super().__init__()
        self._base = base
        self._coffecient = coff
        self._type = 'exp'
        self._exp = 1
        self._operand = '**'
        self._name = 'exp'
        self._constant = constant
    def __pow__(self, other):
        #(ka^m )** n = k^n * a^mn
        if(type(other) in (int, float)):   #x^0 = 1
            #return a constant object
            base = self._base * other
            coff = self._coffecient  ** other
            return (base, self._coffecient)
        if(type(other)  == Basic):
            #build the base based on the power
            return e(other,self._coffecient,self._constant)
        #Ex y = 2*(2x+1)^3
    def __rpow__(self, other):
        return self.__pow__(other)               
    #  df/dx for f = ax^n  = anx^(n-1) * d(x)/dx
    def __add__(self,other):
        #Add or subtract all constanst
        #If is same object add them up
        if(type(other) == int or type(other) == float or \
                    type(other)== Constant):
            if(type(other)== Constant):  other_c = other._constant
            else:  other_c = other
            self._constant +=  other_c          
            return self
        if(self.__eq__(other) == True ):
            self._coffecient  +=  other._coffecient
            return self
       #If is different  objects create series
        series  = Series()
        series.add(self)
        series.add(oper('__add__'))
        series.add(other)
        return series
    def __radd__(self, other):
        return self.__add__(other)
    def __sub__(self,other):
        #Add or subtract all constanst
        #If is same object add them up
        if(type(other) == int or type(other) == float or \
                    type(other)== Constant):
            if(type(other)== Constant):  other_c = other._constant
            else:  other_c = other
            self._constant -=  other_c          
            return self
        if(self.__eq__(other) == True ):
            self._coffecient  -=  other._coffecient
            return self
       #If is different  objects create series
        series  = Series()
        series.add(self)
        series.add(oper('__sub__'))
        series.add(other)
    def __rsub__(self, other):
        return self.__sub__(other)
   
    def __pow__(self, other):
        #(ka^m )** n = k^n * a^mn
        #print('Iama in __POW__', type(self),type(other),other,self.__dict__)
        if(other ==0):   #x^0 = 1
            #return a constant object
            const = Constant(self._coffecient )
            return const
        if (self._constant == 0 ):
            exp = self._exp * other
            coff = self._coffecient ** other
            return power(self._base,exp,coff)
        #Ex y = 2*(2x+1)^3
        else :
            #Create a new base
            #re-adjust the base
            #exp = self._exp * other
            exp =  other
            coff = 1
            constant = 0
            return power(self,exp,coff,constant)
    #def __rpow__(self, other):
    #    return self.__pow__(other)
   
    def __mul__(self, other):
        if(type(other) == int or type(other) == float or \
                    type(other)== Constant):
            if(type(other)== Constant):  other_c = other._constant
            else:  other_c = other
            self._coffecient *= other
            return self
        if(self.__eq__(other) == True and self._constant == 0 and \
                      other._constant == 0 ):
            base = self._base + other._base
            coff = self._coffecient * other._coffecient        
            expObj = exp(base,coff)
            return expObj
        #If is different  objects create series
       
        series  = Series()
        series.add(self)
        series.add(oper('__mul__'))
        series.add(other)
        return series
       
    def __rmul__(self, other):
        return self.__mul__(other)
    def __truediv__(self, other):
        if(type(other) == int or type(other) == float or \
                    type(other)== Constant):
            if(type(other)== Constant):  other_c = other._constant
            else:  other_c = other
            self._coffecient /= other
            return self
        if(self.__eq__(other) == True and self._constant == 0 and \
                      other._constant == 0 ):
            base = self._base - other._base
            coff = self._coffecient / other._coffecient        
            expObj = exp(base,coff)
            return expObj
        #If is different  objects create series   
        series  = Series()
        series.add(self)
        series.add(oper('__truediv__'))
        series.add(other)
        return series
       
    def __rtruediv__(self, other):
        return self.__truediv__(other)
    def derivative(self):
        #Create a power object
        coff = self._coffecient
        exp1 = self._exp
        const = self._constant
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        fprime = exp (base,coff,const)
        gprime = base.derivative()
        result = fprime * gprime
        return result
    def integrate(self):
        series = Series()
        #integrate lnx = xln(x) -x
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        coff = self._coffecient
        exp1 = self._exp
        const = self._constant

        fint  = exp(base,coff)
        gprime = base.derivative()
       
        coff = 1
        if ( type(gprime) == Constant or type(gprime)== float or \
                                         type(gprime)== int ):
            if (type(gprime) == Constant):
                coff = gprime._constant
            elif(type(gprime)== float or type(gprime)== int):
                coff = gprime
            fint  /= coff
       
        return fint
class ln(Element):
   
    def  __init__(self, base, coff = 1, constant = 0):
        #if (isinstance(base,Element) != True and type(base) != None):
        #   raise TypeError("input must be a Element or None ")
        super().__init__()
        self._base = base
        self._coffecient = coff
        self._type = 'ln'
        self._exp = 1
        self._name = 'ln'
        self._constant = constant
        self._base = base
                         
    #  df/dx for f = ax^n  = anx^(n-1) * d(x)/dx
    def derivative(self):
        #Create a power object
        coff = self._coffecient
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        exp = -1
        fprime = power (base,exp ,coff)
        op = oper('__mul__')
        gprime = base.derivative()
       
        result = fprime * gprime
        return result
    def integrate(self):
        series = Series()
        #integrate lnx = xln(x) -x
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        pow_x = power(base, 1, self._coffecient)
        lnx = ln(base,self._coffecient)
        gprime = base.derivative()
        series.add(pow_x)
        series.add(oper('__mul__'))
        series.add(lnx)
        series.add(oper('__sub__'))
        series.add(pow_x)
        if (self._constant != 0 ):
            const = Constant(const)
            pow_c = const.integrate()
            series.add(oper('__add__'))
            series.add(pow_c)
        return series
       
class power(Element):
   
    def  __init__(self, base, exp, coff, constant = 0):
        #if (isinstance(base,Element) != True and type(base) != None):
        #   raise TypeError("input must be a Element or None ")
        super().__init__()
        self._base = base
        self._coffecient = coff
        self._type = 'power'
        self._exp = exp
        self._operand = '**'
        self._name = 'x'
        self._constant = constant
        self._base = base
                         
    #  df/dx for f = ax^n  = anx^(n-1) * d(x)/dx
    def derivative(self):
        #Create a power object
        exp = self._exp-1
        coff = self._coffecient * self._exp
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        if ( exp  == 0 ):
            fprime =  coff
        else :
            fprime = power(base,exp,coff)
        #fprime = self._coffecient * self._exp * base ** (self._exp-1)
        op = oper('__mul__')
        gprime = base.derivative()
        result = fprime * gprime
        return result
    def integrate(self):
        #integrate x^n = x^(n+1)/(n+1)
        #Create a power object
        exp = self._exp+1
        if(exp == 0 ):
            coff = self._coffecient
        else:
            coff = self._coffecient /exp
        const = self._constant
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        fint =  power(base,exp,coff)
        gprime = base.derivative()
        coff =1
        if ( type(gprime) == Constant or type(gprime)== float or \
                                         type(gprime)== int ):
            if (type(gprime) == Constant): coff = gprime._coffecient
            elif(type(gprime)== float or type(gprime)== int):
                coff = gprime
        fint  /= coff
        if (const == 0 ):
            return fint
        else :
            const = Constant(const)
            pow_c = const.integrate()
   
            #Create series
            series  = Series()
            series.add(fint)
            series.add(oper('__add__'))
            series.add(pow_c)
            return series
       
       
class trig(Element):
    def  __init__(self, base,coff=1,constant =0):
        if (isinstance(base,Element) != True ):
           raise TypeError("Input must be Element ")
        super().__init__()
        self._base = base
        self._coffecient = coff
        self._type = ""
        self._name = ""
        self._exp= 1
        self._constant = constant
        self._base = base
          
    #  df/dx for f = acox(x)  = -asin(x)
    def derivative(self):
        pass
   
    def __add__(self,other):
        #Add or subtract all constanst
        #If is same object add them up
        if(type(other) == int or type(other) == float or \
                    type(other)== Constant):
            if(type(other)== Constant):  other_c = other._constant
            else:  other_c = other
            self._constant += other_c          
            return self
        if(self.__eq__(other) == True):
            self._coffecient  += other
            return self
       #If is different  objects create series
        series  = Series()
        series.add(self)
        series.add(oper('__add__'))
        series.add(other)
        return series
    def __radd__(self, other):
        return self.__add__(other)
    def __sub__(self,other):
        #Add or subtract all constanst
        #If is same object add them up
        if(type(other) == int or type(other) == float or \
                    type(other)== Constant):
            if(type(other)== Constant):  other_c = other._constant
            else:  other_c = other
            self._constant -= other_c          
            return self
        if(self.__eq__(other) == True):
            self._coffecient  -= other
            return self
       #If is different  objects create series
        series  = Series()
        series.add(self)
        series.add(oper('__sub__'))
        series.add(other)
        return series
    def __rsub__(self, other):
        return self.__sub__(other)
   
    def __pow__(self, other):
        #(ka^m )** n = k^n * a^mn
        #print('Iama in __POW__', type(self),type(other),other,self.__dict__)
        if(other ==0):   #x^0 = 1
            #return a constant object
            const = Constant(self._coffecient )
            return const
        if (self._constant == 0 ):
            exp = self._exp * other
            coff = self._coffecient ** other
            return power(self,exp,coff)
    def __rpow__(self, other):
        return self.__pow__(other)
   
    def __mul__(self, other):
        if(type(other) == int or type(other) == float or \
                    type(other)== Constant):
            if(type(other)== Constant):  other_c = other._constant
            else:  other_c = other
            self._coffecient *= other_c
            return self
        if(self.__eq__(other) == True and self._constant == 0 and \
                      other._constant == 0 ):
            exp = self._exp + other._exp
            coff = self._coffecient * other._coffecient        
            pow = power(self,exp,coff)
            return pow
        #If is different  objects create series
       
        series  = Series()
        series.add(self)
        series.add(oper('__mul__'))
        series.add(other)
        return series
       
    def __rmul__(self, other):
        return self.__mul__(other)
    def __truediv__(self, other):
        if(type(other) == int or type(other) == float or \
                    type(other)== Constant):
            if(type(other)== Constant):  other_c = other._constant
            else:  other_c = other
            self._coffecient /= other_c
            return self
        if(self.__eq__(other) == True and self._constant == 0 and \
                      other._constant == 0 ):
            exp = self._exp - other._exp
            coff = self._coffecient / other._coffecient        
            pow = power(self,exp,coff)
            return pow
        #If is different  objects create series
       
        series  = Series()
        series.add(self)
        series.add(oper('__truediv__'))
        series.add(other)
        return series
       
    def __rtruediv__(self, other):
        return self.__truediv__(other)
class sin(trig):
    def  __init__(self, base,coff=1,constant =0):
        if (isinstance(base,Element) != True ):
           raise TypeError("Input must be Element ")
        super().__init__(base,coff,constant)      
        self._type = 'sin'
        self._name = 'sin'
          
    #  df/dx for f = asin(x)  = acos(x)
    def derivative(self):
        #Create a sin object
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        fprime = self._coffecient * cos(base)
        op = oper('__mul__')
        gprime = base.derivative()
        result = fprime * gprime
        return result
    def integrate (self):
        #Create a sin object
        const = self._constant
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        fint = -1 * self._coffecient * cos(base)
        gprime = base.derivative()

        if ( type(gprime) == Constant or type(gprime)== float or \
                                         type(gprime)== int ):
            if (type(gprime) == Constant):
                coff = gprime._constant
            elif(type(gprime)== float or type(gprime)== int):
                coff = gprime
            fint  /= coff
        if (const == 0 ):
            return fint
        else :
            const = Constant(const)
            pow_c = const.integrate()
   
            #Create series
            series  = Series()
            series.add(fint)
            series.add(oper('__add__'))
            series.add(pow_c)
            return series

class cos(trig):
    def  __init__(self, base,coff=1,constant =0):
        if (isinstance(base,Element) != True ):
           raise TypeError("Input must be Element ")
        super().__init__(base,coff,constant )
        self._type = 'cos'
        self._name = 'cos'
          
    #  df/dx for f = acox(x)  = -asin(x)
    def derivative(self):
        #Create a sin object
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        fprime = self._coffecient * -1 * sin(base)
        op = oper('__mul__')
        gprime = base.derivative()
        result = fprime * gprime
        return result
    def integrate (self):
        #Create a sin object
        const = self._constant
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        fint =  self._coffecient * sin(base)
        gprime = base.derivative()
        if ( type(gprime) == Constant or type(gprime)== float or \
                                         type(gprime)== int ):
            if (type(gprime) == Constant): coff = gprime._constant
            elif(type(gprime)== float or type(gprime)== int):
                coff = gprime
            fint  /= coff
        if (const == 0 ):
            return fint
        else :
            const = Constant(const)
            pow_c = const.integrate()
   
            #Create series
            series  = Series()
            series.add(fint)
            series.add(oper('__add__'))
            series.add(pow_c)
            return series
       
class tan(trig):
    def  __init__(self, base,coff=1,constant =0):
        if (isinstance(base,Element) != True ):
           raise TypeError("Input must be Element ")
        super().__init__(base,coff,constant)
        self._type = 'tan'
        self._name = 'tan'
          
    #  df/dx for f = a * tan(x)  = a *sec(x)**2
    def derivative(self):
        #Create a sin object
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        #
        sec_base = sec(base)
        exp = 2
        fprime =  power(sec_base,exp,self._coffecient)
        op = oper('__mul__')
        gprime = base.derivative()
        result = fprime * gprime
        return result
    def integrate(self):
        #Create a sin object
        const = self._constant
        none = Negator()
        if ( none == self._base):
            base = cos('x')
        else :
            base = cos(self._base)
       
        fint =  ln(base, -1 * self._coffecient)
        gprime = base.derivative()
        if ( type(gprime) == Constant or type(gprime)== float or \
                                         type(gprime)== int ):
            if (type(gprime) == Constant): coff = gprime._coffecient
            elif(type(gprime)== float or type(gprime)== int):
                coff = gprime
               
            fint  /= coff
        if (const == 0 ):
            return fint
        else :
            const = Constant(const)
            pow_c = const.integrate()
   
            #Create series
            series  = Series()
            series.add(fint)
            series.add(oper('__add__'))
            series.add(pow_c)
            return series
       
class sec(trig):
    def  __init__(self, base,coff=1,constant =0):
        if (isinstance(base,Element) != True ):
           raise TypeError("Input must be Element ")
        super().__init__(base,coff,constant)
        self._type = 'sec'
        self._name = 'sec'
          
    #  df/dx for f = a * sec(x)  = a *sec(x)*tan(x)
    def derivative(self):
        #Create a sin object
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        sec_base = sec(base)
        tan_base = tan(base)
        fprime = sec_base * tan_base
        op = oper('__mul__')
        gprime = base.derivative()
        result = fprime * gprime
        return result
    def integrate(self):
         #Create a Sec Object  object
        const = self._constant
        none = Negator()
        if ( none == self._base):
            base = Basic('x')
        else :
            base = self._base
        fint =  self._coffecient * sin(base)
        gprime = base.derivative()
        if ( type(gprime) == Constant or type(gprime)== float or \
                                         type(gprime)== int ):
            if (type(gprime) == Constant): coff = gprime._coffecient
            elif(type(gprime)== float or type(gprime)== int):
                coff = gprime
        fint  /= coff
        if (const == 0 ):
            return fint
        else :
            const = Constant(const)
            pow_c = const.integrate()
   
            #Create series
            series  = Series('integrate')
            series.add(fint)
            series.add(oper('__add__'))
            series.add(pow_c)
            return series
class Series():
    #Empty Series
    def __init__(self, sType = ""):
        self._elements = []
        self._type = sType
   
    def __add__(self, other):
        self._elements.append(oper('__add__'))
        self._elements.append(other)
        return self
    def __radd__(self,other):
        return self.__add__(other)
    def __sub__(self, other):
        self._elements.append(oper('__sub__'))
        self._elements.append(other)
        return self
    def __rsub__(self,other):
        return self.__sub__(other)
   
    def __mul__(self, other):
        self._elements.append(oper('__mul__'))
        self._elements.append(other)
        return self
    def __rmul__(self,other):
        return self.__mul__(other)
    def __truediv__(self, other):
        self._elements.append(oper('__truediv__'))
        self._elements.append(other)
        return self
    def __rtruediv__(self,other):
        return self.__truediv__(other)
    #Add element to the series
    def add(self,basic):
        if(isinstance(basic,Element) == True):
            self._elements.append(basic)
        elif(isinstance(basic,Series) == True):
            for elem in basic._elements:
                self.add(elem)
        elif(type(basic) == str):
            self._elements.append(basic)
   
    def multiplyWith(self, const):
        index = 0
        carry = True
        while (index < len(self._elements)):
            elem = self._elements[index]
            last = (index == len(self._elements)-1)
            if (isinstance(elem, Element)):
                if(carry == True): elem *= const
                if(last != True ):
                    nextElem = self._elements[index+1]
                    if (type(nextElem) == str ):
                        if(nextElem == oper('__add__') or \
                                nextElem == oper('__sub__')):
                                carry = True
                                index += 1
                                continue
                        elif(nextElem == oper('__mul__') or \
                                nextElem == oper('__truediv__')):
                                carry = False
                                index += 1
                                continue
            index += 1
    def __str__(self):
        lines = ""
        for e in self._elements  :
            if(type(e) != str):
                lines += ('('+str(e) +')')
            else :
                lines += str(e)
        result = str(lines).replace('(1)*','')
        return result
    def toString(self):
        lines = ""
        for e in self._elements  :
            if(type(e) != str):
                lines += e.toString(False)
            else :
                lines += str(e)
        result = str(lines).replace('(1)*', "")
        return result
    def __repr__(self):
        lines = []
        for e in self._elements :
            lines.append(str(e))
        return lines
    def domain (self):
        lines = set()
        for elem in self._elements :
            if(isinstance(elem,Element)):
                lines.add(str(elem.domain()))
        return list(lines)
    def kindOf(self, other):
        #Need to implement
        return False
    def deriv_uv (self, listExtract ):
        # (uvwx)' = u'vwx + uv'wx+ uvw'x + uvwx'
        series  =  Series()
        for i1  in range(len(listExtract)):
            elem = listExtract[i1]
            if(isinstance(elem,Element) == True):
                result  = elem.derivative()
                #print('D-Element-UV=',elem,type(elem),type(result), result)
                #print('elem=',elem,'prime=',result, type(result))
                series.add(result)
                product = 1
                for i2 in range(len(listExtract)):
                    if(i1 != i2): product *= listExtract[i2]
                #print('D-Product=',product,type(product))
                series.add(oper('__mul__'))
                series.add(product)
                #don't add + to last element
                if (i1 < len(listExtract) -1): series.add(oper('__add__'))
        return series
    def printAll(self):
        index = 0
        for elem in self._elements:
            index += 1
            #print(type(elem),len(self._elements) , 'Element=', index, elem)
    def deriv_list(self, listExtract):
        #Ex: y=  x * sin(x) + cos(x) case case 5
        #Ex: y=  (x * sin(lnx))/cos(x) case 6
        #ex: y= x/lnx + sin(x)*x  case 5
        #ex: y = x * sin(x) * cos(x)
        deriv  = Series()
        if(len(listExtract) == 0 ): return deriv
       
        #convert all division to multiplication
        # x * y / z *k/d = x * (1/y) + k * (1/d)
        listMult = []
        operand = ''
        div = 1
        for elem  in listExtract:
            #print('elem=',type(elem),elem,'operand=',operand)
            if(isinstance(elem,Element) == True):
                if (operand == '' or operand == oper('__mul__')):
                    listMult.append(elem)
                elif (operand == '' or operand == oper('__truediv__')):
                    result = elem ** -1
                    #print('result',type(result), result)
                    listMult.append(result)
            elif (type(elem) == str ):
                operand = elem
                #print('Debugging operand', operand, elem)
              
        if(len(listMult) > 0):
            #print('listMult',type(listMult), listMult)
            result = self.deriv_uv(listMult)
            #print('D-UV=',listMult,type(listMult),type(result), result)
            deriv.add(result)
            return deriv
    def chooseUV( self,elem1, elem2):
        (eType1,eType2) = ("", "")
        if (isinstance(elem1, Element )):
            eType1 = elem1._type
        if (isinstance(elem2, Element ) ):
            eType2 = elem2._type
        if (eType1 != "" and eType2 != "" ):
            prio1 = integ_prio(eType1)
            prio2 = integ_prio(eType2)
        if (prio1 > prio2): return (elem1, elem2)
        if (prio2 > prio1): return (elem2, elem1)
        if (prio1 == prio2):
            if(elem1._exp >= elem2._exp ):
                return (elem1,elem2)
            else : return (elem1,elem2)
    def productIsSame(self, u, v, d_elem, i_elem):
         
        if ( isinstance(u,Element) and u.kindOf(d_elem)):
            print(" productIsSame u and d_elem")
            if (isinstance(v,Element)  and v.kindOf(i_elem) ):
                print(" productIsSame v and i_elem")
                coff = (d_elem._coffecient * i_elem._coffecient) /  \
                      (u._coffecient * v._coffecient)
            return coff
    def productIsIntegral(self, d_elem, i_elem):
        product =  d_elem * i_elem
        integ = None
        if (isinstance(product,Element )):
           integ = product.integrate()
        return integ
       
    def integrate_byparts(self,listMult):
        # Supports specific cases integration by parts ,
        # I wilsh I would have had more time
        #integral (uv)  = u * integral(v) - integral( u ' * integral(v))
        #ex: integral(x sin(x) dx u = x v sin(x),
        #ex: integral(xln(x)) dx u = ln(x) , v = x
        #ex: integral((x+2)*exp(x)) u= (x+2) v = exp(x)
        #ex: Integral (x**2 * cos(x) dx u= x**2 v = cos(x)
        #ex: integral (x ^2) exp(x) dex  u = x^2 v =exp(x)
        #ex: Integral (x ** 0.5 ln(x) dx u = ln(x) v= x ** 0.5)
        #ex: Integrl cos(x) exp(x) u = cos(x) v = exp(x)
        #ex: Integral cos(x)sin(x)  u = cos(x) v = sin(x)
        #Prioritize the uv selection
        # Using ILate, I inverse , L = ln ,a = Algebric , t = trig , e = expo
        elem1 =  listMult[0]
        elem2 =  listMult[1]
       
        (u,v)  =  self.chooseUV (elem1,elem2 )
        print (" u=  ", u )
        print (" v=  ", v )
        # Following tabular integration by parts
        #Rule 1
        #Tricks: If one of the functions is a polynomial (say nth order) and
        # the other is integrable n times, then you can use the fast and easy Tabular Method:
        #
        series_i = Series('integrate')
        series_d = Series('derivative')
        count = 0
        integ  =  Series()
        #Start with u and v in the list
        series_d.add(u)
        series_i.add(v)
        (prev_d_elem,prev_i_elem,d_elem,i_elem) = ("","","","")
        integ_method = ""
        isValid = False
        additional_integ = None
        while ( count < 10 ):
            count += 1 # decrement , safety purpose, Don't exceed 10 derivatives
           
            if (prev_d_elem == ""):
                d_elem = u.derivative()
               
            else:
                d_elem = prev_d_elem.derivative()
            prev_d_elem = d_elem
   
            series_d.add(d_elem)
           
            if (prev_i_elem == ""):
                i_elem = v.integrate()
            else:
                i_elem = prev_i_elem.integrate()
           
            prev_i_elem = i_elem
            series_i.add(i_elem)
            product = d_elem * i_elem
            #print(count," derivative  d= ", d_elem ," Integrate i= ", i_elem, type(product),product)
            if (d_elem == 0 ):
                integ_method = 'integrate_byparts_type1'
                isValid = True
                #stop comuting the derivative until it becomes zero for power series
                break
            if (count >= 2):
                additional_integ = self.productIsIntegral(d_elem,i_elem)
                #product of the last row should be integratable
                if( additional_integ != None ):
                        #isinstance (product , Series ) ):
                    integ_method = 'integrate_byparts_type2'
                    isValid = True
                    #stop computing once product (d_elem * i_elem is integratable)
                    break
                additional_integ = self.productIsSame(u,v, d_elem,i_elem)
                if(additional_integ != None ):
                        #isinstance (product , Series ) ):
                    integ_method = 'integrate_byparts_type3'
                    isValid = True
                    #stop computing the once same uv is repeated
                    break
        if ( isValid ):
            #print('integrate_byparts is valid = ', isValid, " ",integ_method)
            for  index  in range (len(series_d._elements)):
                lastButOne = (index == (len(series_d._elements) -2))
                #if (index > (len(series_d._elements) -2)): break
                u_elem = series_d._elements[index]
                v_elem = series_i._elements[index + 1]
                #Every second element multiply with -1
                if(index % 2 == 1):
                    u_elem *= -1
                if (type(u_elem) == Constant ):
                    result = u_elem._constant * v_elem
                else:
                    result = u_elem * v_elem
                integ.add(result)
               
                if (lastButOne != True):
                    integ.add(oper('__add__'))
                else :
                    #Check any addition Integation or coffecient to be added
                    if(additional_integ != None ):
                        #print('adiitional_integ = ', additional_integ ,\
                                  #"integ_method=", integ_method)
                        if(integ_method == 'integrate_byparts_type2'):
                            integ.add(oper('__add__'))
                            integ.add(additional_integ)      
                        elif(integ_method == 'integrate_byparts_type3'):
                            mult = 1/((additional_integ * -1) +1 )
                            integ.multiplyWith(mult)
                #print (index,'/',len(series_d._elements) ,' u-lem =', u_elem,\
                      #" v-elm= ", v_elem , " product= " ,type(result), result )
                if (lastButOne): break
   
        return integ
  
    def integrate_substitution (self,listMult):
        #currently suports only one substitution
        #integral(f(g(x))) g'(x) dx )  = f(g(x)
        last = False
        index = 0
        integs = Series()
        currEPow = None
        #Need to create separate function , I don't much time now
        #Cleanup later
        trial = 2
        while ( trial >  0 ):
            if (trial == 2):
                #Ex: y= sin^2(x) * cos(x)  curr = sin(x) , next = cos(x)
                #curr' = next  u = sin(x) , u' = cos(x) y= integral(u^2)
                currE =  listMult[index]
                nextE  = listMult[index+1]
            else:
                #try reversing the order
                #Ex: y= cos(x) * sin^2(x)    curr = cos(x) , next = sin(x)
                #next' = curr  u = sin(x) , u' = cos(x) y= integral(u^2)
                nextE =  listMult[index]
                currE  = listMult[index+1]
            trial -= 1
            if(currE._base  != None ):
                deriv_base_curr = currE._base.derivative()
            else: continue
            deriv_next = nextE.derivative()
            
            if (isinstance(currE, power) == True):
                if(deriv_base_curr.kindOf(nextE)):
                    currEPow = currE
                    break
            elif (isinstance(currE, trig) == True):
                if(deriv_base_curr.kindOf(nextE)):
                    currEPow = currE
                    break
            if (currEPow == None):
                #Try with  build power object
                if (isinstance(currE, Element ) == True):
                    exp = currE._exp
                    coff = currE._coffecient
                    currEPow = power (currE,exp, coff)
                    deriv_base_curr = currEPow._base.derivative()                   
                    if (deriv_base_curr.kindOf(nextE)):
                        break
        if (currEPow == None ):
            return integs
        #Ex: y= x * (sin(x**2)) prev = x , next = sin(x**2)
        # next.base' = prev , u= x**2 du'= 2*x , du = y = integral(u du/2 )
        #Check prev is
        #Ex: y= cos(x) * sin(x)  prev = cos(x) , next = sin(x)
        # next' = prev  u = sin(x) , u' = cos(x) y= integral(u)
        deriv_base_curr = currEPow._base.derivative()
        deriv_next = nextE.derivative()
        #Ex: y= (x**2+1) * x   prev = (x**2+1) , next = x
        # prev' = next  u = (x**2+1) , u' = 2*x  y= integral(u), missMult=2
        #Check prev is
        if(deriv_base_curr.kindOf(nextE)):
            missMult = nextE._coffecient/deriv_base_curr._coffecient
            currEPow *= missMult
            result = currEPow.integrate()
            integs.add(result)
            #print('integrate_substitution result = ',integs, missMult,nextE._coffecient,deriv_base_curr._coffecient)
        return integs
    def integrate_list(self, listExtract):
        integ_series = Series()
        if(len(listExtract) == 0 ): return integ
       
        #convert all division to multiplication
        # x * y / z + k/d = x * (1/y) + k * (1/d)
        listMult = []
        operand = ''
        div = 1
        for elem  in listExtract:
            #print('elem=',type(elem),elem,'operand=',operand)
            if(isinstance(elem,Element) == True):
                if (operand == '' or operand == oper('__mul__')):
                    listMult.append(elem)
                elif (operand == '' or operand == oper('__truediv__')):
                    result = elem ** -1
                    #print('result',type(result), result)
                    listMult.append(result)
            elif (type(elem) == str ):
                operand = elem
                #print('Debugging operand', operand, elem)
              
        if(len(listMult) > 0):
            #for e in listMult:
                #Verify expression is substitution candidate
            result = self.integrate_substitution (listMult)
            if (result == None  or (type(result) == Series and
                             len(result._elements) ==0)):
                result = self.integrate_byparts (listMult)
            integ_series.add(result)
        return integ_series
    def integrate (self):
        integrate  = Series()
        index = 0
        multdivList = []
        while (index < len(self._elements)):
            elem = self._elements[index]
            last = (index == len(self._elements)-1)
            #Special case process elements bracket first
            #print('Series-elem=',elem,index,type(elem))
            if(elem == oper('__perl__')):
                #find the matching  bracket ")"
                peren_end = list.find(oper('__perr__'))
                extract = self._elements[elem:paren_end]
                result = self.integrate(extract, result)
                integrate.add(result)
                index += peren_end + 1
            elif (isinstance(elem, Element)):
                if(last != True ):
                    nextElem = self._elements[index+1]
                    if (type(nextElem) == str ):
                        if(nextElem == oper('__add__') or \
                                nextElem == oper('__sub__')):
                            result = elem.integrate()
                            integrate.add(result)  #case1
                        elif(nextElem == oper('__mul__') or \
                                nextElem == oper('__truediv__')):
                            multdivList.append(elem)
                else:  # last element
                    if (len(multdivList) > 0): #case 2,4,5,6
                        multdivList.append(elem)
                        #Call uv or u/v  using derivative(list)
                        result = self.integrate_list(multdivList)
                        integrate.add(result)
                    else:   #last element in the case 1,3
                        result = elem.integrate()
                        #print('D-Element=',elem,type(elem),type(result), result)
                        integrate.add(result)
                index += 1
            elif (type(elem) == str ):
                #If lst element is is constant , don't put any operand
                #derivative of constant is zero
                isLastConstant = False
                if(last != True):
                    nextElem = self._elements[index+1]
                    if(type(nextElem)== int or type(nextElem)== float):
                        isLastConstant = True
                if(isLastConstant != True):
                    if ( elem == oper('__add__') or elem == oper('__sub__')):
                        if (len(multdivList) == 0):  integrate.add(elem) # case1, 3
                    elif(elem == oper('__mul__') or \
                              elem == oper('__truediv__')):
                        multdivList.append(elem)  # case 2 , 4, 5, 6
               
                index += 1
            elif(type(elem)== int or type(elem)== float):
                index += 1
        #print('D-deriv=',self,type(self),type(deriv), deriv)
        return integrate
    #############################################
    def derivative(self):
        #Traverse  through all the elements in the list
        #1. process all the elements with in ( ..... ) first
        #2. Process exp(**)
        #3. process div (/) or div (*) whichever comes first
        #4. Process (+) or process (-) whichever comes first
        #Empty the list after processing
        #print('Derivative calc starts from here ')
        deriv = Series()
        index = 0
        count = 0
        multdivList = []
        while (index < len(self._elements)):
            elem = self._elements[index]
            last = (index == len(self._elements)-1)
            #Special case process elements bracket first
            #print('Series-elem=',elem,index,type(elem))
            if(elem == oper('__perl__')):
                #find the matching  bracket ")"
                peren_end = list.find(oper('__perr__'))
                extract = self._elements[elem:paren_end]
                result = self.derivative(extract, result)
                deriv.add(result)
                index += peren_end + 1
            elif (isinstance(elem, Element)):
                #check next element is '+', '-'
                #Prevent the crash (index oout of range )
                # if it is not last element, process
                #case 1 ,Element ,next element is + or - but not last
                #case 2 ,Element ,next element is * or / but not last
                #case 3 ,Element ,next element is + or - but  last
                #case 4, Element ,next element is * or / but  last
                #Ex: y = x + sin(x) + tan(x) , case 1,3
                #Ex: y = x * sin(x) * tan(x) , case 2
                #Ex: y = x / sin(x)  , case 2 ,4
                #Ex: y=  x * sin(x) + cos(x) case case 5
                #Ex: y=  (x * sin(x))/cos(x) case 6
                #ex: y= x/lnx + sin(x)*x  case 5
                #ex: y = x * sin(x) * cos(x)
                if(last != True ):
                    nextElem = self._elements[index+1]
                    if (type(nextElem) == str ):
                        if(nextElem == oper('__add__') or \
                                nextElem == oper('__sub__')):
                            if(len(multdivList) == 0):
                                result = elem.derivative()
                                #print('D-Element=',elem,type(elem),type(result), result)
                                deriv.add(result)  #case1
                            else :
                                multdivList.append(elem)
                                #Call uv or u/v  using derivative(list)
                                result = self.deriv_list(multdivList)
                                #print('D-Dlist=',multdivList,type(result), result)
                                deriv.add(result)
                                multdivList.clear()
                        elif(nextElem == oper('__mul__') or \
                                nextElem == oper('__truediv__')):
                            multdivList.append(elem)
                else:  # last element
                    if (len(multdivList) > 0): #case 2,4,5,6
                        multdivList.append(elem)
                        #Call uv or u/v  using derivative(list)
                        result = self.deriv_list(multdivList)
                        #print('D-Dlist=',multdivList,type(multdivList),type(result), result)
                        deriv.add(result)
                    else:   #last element in the case 1,3
                        result = elem.derivative()
                        #print('D-Element=',elem,type(elem),type(result), result)
                        deriv.add(result)
                index += 1
            elif (type(elem) == str ):
                #If lst element is is constant , don't put any operand
                #derivative of constant is zero
                isLastConstant = False
                if(last != True):
                    nextElem = self._elements[index+1]
                    if(type(nextElem)== int or type(nextElem)== float):
                        isLastConstant = True
                if(isLastConstant != True):
                    if ( elem == oper('__add__') or elem == oper('__sub__')):
                        if (len(multdivList) == 0):  deriv.add(elem) # case1, 3
                    elif(elem == oper('__mul__') or \
                              elem == oper('__truediv__')):
                        multdivList.append(elem)  # case 2 , 4, 5, 6
               
                index += 1
            elif(type(elem)== int or type(elem)== float):
                index += 1
        #print('D-deriv=',self,type(self),type(deriv), deriv)
        return deriv
    def simplify(self):
        series = Series()
        e =0
        while( e < len(self._elements)):
            elem = self._elements[e]
            index = e
            e += 1
            #print('elem=', index , type(elem), elem)
            if (isinstance(elem, Constant)):
                series.add(elem)
                continue
            elif (isinstance(elem, Element)):
                series.add(elem)
                continue
            elif (type(elem) == int or type(elem) == float):
                series.add(elem)
                continue
            elif (type(elem) == str ):
                if (elem == '-' or elem == '+'):
                    next = self._elements[index + 1]
                    if(next._coffecient < 0):
                        if (elem == '+'):
                            next._coffecient *= (-1)
                            elem = '-'
                            series.add(elem)
                            series.add(next)
                            e +=1
                        elif (elem == '-'):
                            next._coffecient *= (-1)
                            elem = '+'
                            series.add(elem)
                            series.add(next)
                            e +=1
                    else:
                        series.add(elem)
                    continue
           
            if (type(elem) == str and (elem == '*' or elem == '/')):
                prev = self._elements[index - 1]
                next = self._elements[index + 1]
                valuePrev = None
                valueNext = None
                value = None
                if (type(prev) == int or type(prev) == float): valuePrev = prev
                elif(type(prev)== Constant): valuePrev = prev._constant
                if (type(next) == int or type(next) == float): valueNext = next
                elif(type(next)== Constant): valueNext = next._constant
                if( valuePrev == None and valueNext == None ):
                    series.add(elem)
                    continue
                elif (valuePrev != None and valueNext != None ):
                    if(elem == '*'): value = valuePrev  * valueNext
                    elif(elem == '/'): value = valuePrev  / valueNext
                    series._elements.pop()
                    const = Constant(value)
                    series.add(const)
                    e += 1
                    continue
                elif (valuePrev != None and isinstance(next, Element) ):
                    if(elem == '*'): next._coffecient * valuePrev
                    elif(elem == '/'): next._coffecient / valuePrev
                    series._elements.pop()
                    if(valuePrev != 0):
                        series.add(next)
                        e += 1
                    else :
                        e += 2
                    continue
                elif (valueNext != None and isinstance(prev, Element) ):
                    if(elem == '*'): prev._coffecient * valueNext
                    elif(elem == '/'): prev._coffecient / valueNext
                    series._elements.pop()
                    if(valueNext != 0):
                        series.add(prev)
                        e += 1
                    else :
                        e += 2
                    continue
        return series
'''
x= Basic('x')
y= 3*x**2 -4*x +7
print(y, type(y), y.derivative())
y= (x-1)/(x-3)
print(y, type(y), y.integrate())

y= (3*x**2 -4*x +7)/(x-1)
print(y, type(y), y.derivative())
y= (3*x**2 -4*x +7)/(2*x**2 -3*x +2 )
print(y, type(y))
y= ln(x) +ln (x)
print( 'AAAAAA', type(y),y.__dict__)
y= x * cos(x)
print('y=', y, 'derivative=',y.derivative() ,'integrate=', y.integrate(),'domain =',y.domain())
print ('****************************************************************')
d  = y.derivative()
dd = y.derivative().derivative()
ddd = y.derivative().derivative().derivative()
print(d, 'Simplified=' ,d.simplify().simplify().toString())
print(dd, 'Simplified=', dd.simplify().simplify().toString())
print(ddd, 'Simplified=' ,ddd.simplify().simplify().toString())
'''
'''
x = Basic('x')
print('x=', x, 'derivative=', x.derivative(),'integrate =',x.integrate(),'domain =',x.domain())
y = 2 *x + 1
print('y=', y, 'derivative=',y.derivative() ,'integrate=', y.integrate(),'domain =',y.domain())
print('roots  = ',rootsF(lambda x: 2 *x + 1))
y= 2*x**3 +1
print('y=', y,'derivative=', y.derivative(), 'integrate=', y.integrate(),'domain =',y.domain())
y= 2*(2*x+1)**3 +1
print('y= 2*(2*x+1)**3 +1', y, 'derivative=',y.derivative(),'integrate=',y.integrate(),'domain =',y.domain())
print('roots  = ',rootsF(lambda x: 2*(2*x+1)**3 +1))
y= -2*(3*x-1)**7 -8
print('y= -1*(3*x-1)**7 -8 ', y, 'derivative=',y.derivative(),'integrate=',y.integrate(),'domain =',y.domain())
print('roots  = ',rootsF(lambda x: -2*(3*x-1)**7 -8))
y = sin(x)
print('y=sin(x)', 'y=', y,'derivative=',y.derivative(),'integrate=',y.integrate(),'domain =',y.domain())
y = 3*  sin(4*x+2) +5
print(' 3*sin(4*x+2) +5','y=', y, 'derivative=',y.derivative(),'integrate=' ,y.integrate(),'domain =',y.domain())
y = cos(x)
print('y=cos(x)','y=', y,'derivative=',y.derivative(),'integrate=',y.integrate(),'domain =',y.domain())
y = 3*  cos(4*x-2) +8
print('3* cos(4*x-2) +8','y=', y,'derivative=',y.derivative(),'integrate=',y.integrate(),'domain =',y.domain())
y = tan(x)
print('y=tan(x)','y=', y,'derivative=',y.derivative(),y.integrate(),'domain =',y.domain())
y = sec(x)
print('y=sec(x)','y=', y,'derivative=',y.derivative(),'domain =',y.domain())
y = 5*  tan(3*x+2) -2
print('5*  tan(3*x+2) -2','y=', y,'derivative=',y.derivative(), 'integrate Fail =', y.integrate(),'domain =',y.domain())
y = 3*x**3  +6
print('3*x**2  -5 *x +6', 'y=', y,'derivative=',y.derivative(),'integrate=',y.integrate(),'domain =',y.domain())
y = (x+1) ** 2 + 1
print(" (x+1) ** 2 ",'y=',y, y.derivative(),'integrate=',y.integrate(),'domain =',y.domain())
y = sin(2*x**2 + 1)
print(" sin(2*x**2+1) ",'y=',y, y.derivative(),'integrate Fail =',y.integrate(),'domain =',y.domain())
print('Test case for polynomial .. Starting ...')
y =  5* x **4 + 2 * x ** 3 + 5 * x**2  +8
print("  5* x **4 + 2 * x ** 3 + 5 * x**2  +8 ",y, y.derivative(),'integrate=',y.integrate(),'domain =',y.domain())
y= 2 * sin(x) ** 3  + 2 * sin(x) **2 - 8
#y = sin(x**2 + 4) * x
print("  sin(x) ** 3  + 2 * sin(x) **2 - 8   " ,type(y) , 'derivative=', y.derivative(), 'integrate Fail =',y.integrate(),'domain =',y.domain())

y= sin(x) ** 3  + sin(x) **2 - 8
print("  sin(x) ** 3  - 8 ", y, 'derivative=' ,y.derivative(),'integrate=','integrate Fail =',y.integrate(),'domain =',y.domain())
y= 2 *x * tan(x) ** 3   + 5* sin(x) + x ** 2 
print(" 2 * x* tan(x) ** 3  + 5* sin(x) + x ** 2 " ,y, 'y = ','integrate Fail =', y.derivative()  )

y = sin(x) * cos(x)
print(" sin(x) * cos (x)" , y, 'derivative=' ,y.derivative(), 'integrate=',y.integrate(),'domain =',y.domain())
y = x*sin(x)* cos(x)
print( 'x*sin(x)* cos(x)', y, 'derivative=' ,y.derivative(), 'integrate Fail =',y.integrate(),'domain =',y.domain())
y = x/sin(2*x)
print( 'x/sin(2x)', y, 'derivative=' ,y.derivative(),'integrate Fail =',y.integrate())
y= x
print('Integrate x ', y , y.integrate(),'domain =',y.domain())
y= 2*x**4
print('Integrate  2x^4', y , y.integrate(),'domain =',y.domain())
y= sin(x)
print('Integrate  sin(x)', y , y.integrate(),'domain =',y.domain())
y= cos (x)
print('Integrate  cos(x)', y , y.integrate(),'domain =',y.domain())
print('**************************************Testing lnx ******************************')
y= ln(x)
print(' ln(x) = ', y , y.derivative(), y.integrate(),'domain =',y.domain())
y= ln(2*x-1)
print(' ln(x) = ',y , y.derivative(), y.integrate(),'domain =',y.domain())
y= 5*exp(3*x) + x **2
print(' 5*exp(3*x) ', y,y.derivative(), y.integrate())
y= tan(x)
print(' tan(x) = ', type(y), y , y.derivative(), y.integrate(),'domain =',y.domain())

print ("**************integration substitution testing ******")

y = sin(x) * cos(x)
print('Integrate sin(x) * cos(x) = ', y , y.derivative() , 'Integrate=' , y.integrate())
y = sin(x) ** 3 * cos(x)
print('Integrate sin(x) ** 3 * cos(x) = ', y , y.derivative() , 'Integrate=' , y.integrate())

y=   ((6*x**3+1)**4) *(9 * x**2)
print('Integrate ', y  , y.derivative() , 'Integrate=' , y.integrate())
y = sin(x**2) * x
print('Integrate ', y  , y.derivative() , 'Integrate=' , y.integrate())
y =  cos(x) * sin(x)
print('Integrate sin(x) * cos(x) = ', y , y.derivative() , 'Integrate=' , y.integrate())
y = cos(x) * sin(x) ** 3
print('Integrate sin(x) ** 3 * cos(x) = ', y , y.derivative() , 'Integrate=' , y.integrate())

y=   (9 * x**2) * ((6*x**3+1)**4)
print('Integrate (9 * x**2) * ((6*x**3+1)**4) = ', y  , y.derivative() , 'Integrate=' , y.integrate())
y = sin(x**2) * x
print('Integrate sin(x**2) * x = ', y  , y.derivative() , 'Integrate=' , y.integrate())
y = (5*x + 4)**5
print('Integrate (5*x + 4)**5  * x = ', y  , y.derivative() , 'Integrate=' , y.integrate())
y = 3 * x**2 * (x**3+4) ** 5
print('Integrate 3 * x**2 * (x**3+4) ** 5 = ', y  , y.derivative() , 'Integrate=' , y.integrate())
y= sin(x) **2 * exp(x)
print('Integrate  sin(x) **2 * exp(x) = ', y  , y.derivative() , 'Integrate Fail =' , y.integrate())

print ("********************Testing Integration by Parts *************************")
#Type1
y= x * sin(x)
print('x * sin(x) ' , y,y.derivative(), 'Integrate=' ,y.integrate())
#y= (x+2)*exp(x)
#print('(x+2)*exp(x)'  , y,y.derivative(), 'Integrate=', y.integrate())
y = x
y = (x**2 * cos(x))
print('(x**2 * cos(x)) ' , y,y.derivative(), 'Integrate=', y.integrate())
y= (x ** 2)  * exp(x)
print('(x ** 2)  * exp(x)', y,y.derivative(),'Integrate=', y.integrate())
#type 2
y=  x ** 0.5  * ln(x)
print('x ** 0.5 * ln(x) ' , y,y.derivative(), 'Integrate=', y.integrate())

#type3
y= cos(x)*  exp(x)
print('cos(x)*  exp(x)' , sin(x) , y,y.derivative(),'Integrate=', y.integrate())
'''