#http://www.cs.cmu.edu/~112/schedule.html
def almostEqual(d1, d2, epsilon=10**-5):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1)) < epsilon

#from  derivative_withbase import *
from numpy import linspace, sin, cos, tan,exp,log10

class roots :
    def __init__(self, object ):
        self._function = object
    
    #xn+1 = xn - f(x)/f'(x)
    def __call__(self, x0):
        return self.computeNR(x0)

    def __str__(self):
        return (str(self._function))
    
    def fx(self, x = -1):
        return (self.evaluate(self._function,x))

    def evaluate(self, expr, x):
        #expr = expr.replace('x', 't')
        if 'ln' in expr:
            expr = expr.replace('ln','log10')
        #t = x
        fValue = eval(expr)
        return fValue
    def derivatative(self, x = -1, h = 0.0000005):
        fxh = self.evaluate(self._function, (x+ h))
        fx = self.evaluate(self._function, (x))
        der = ((fxh - fx)/h)
        #print('fxh', fxh, 'fx',fx, h, der)
        return der

    def computeNR(self, x0 = -10):
        
        f= self._function
        
        maxCount = 40
        xn = x0
        count = 0
        pXn1 = None
        #print('NR Method: %s  %s' %('Xn1','Xn'))  
        while (count < maxCount ):
            count += 1
            f =  self.fx(xn)
            dfx = self.derivatative(xn)
            xn1 = (xn) - (f/dfx)
            #print('function',xn1,xn,f,dfx)
            #print('NR Method: %f  %f' %(xn1,xn))  
            if ( pXn1 != None):
                if ( almostEqual(pXn1, xn1 )):
                    return round(xn1,4)
            pXn1 = xn1
            xn   = xn1
        return 'No root, Max Count Exceeded'

def getFactors(num):
    factors = []
    denom = 1
    while (denom <= num):
        if(num % denom == 0): factors.append(denom)
        denom += 1 
    return factors

def rationalRoot(polynomial):
    const = abs(polynomial[len(polynomial)-1])
    leading = abs(polynomial[0])

    constF   = getFactors(const)
    leadingF = getFactors(leading)

    potenF = set()
    #p/q = factors of (const)/factors of (leading)
    for c_el in constF:
        for l_el in leadingF :
            potenF.add(float(c_el/l_el))
    
    potenF = list(potenF)
    potenF.sort()
    factors = []
    #Evaluate each each root with polynomial
    for  e in potenF:
        index = len (polynomial)-1
        fox = 0
        while (index >=0 ):
            fox  += polynomial[index] * e**(len (polynomial)-index-1)
            #print( polynomial[index],(len (polynomial)-index-1),index, fox )
            index -= 1
        #print('computing polynomail: ' , polynomial , 'param=', e, 'value =', fox)
        if ( fox == 0.0):
            factors.append(e)
    return factors

def longDivision(polynomial, root):
    '''
    y= 8*x**4 - 6*x**3 + 4*x**2 + 2 * x**2 -8
    1 | 8 -6 4 2 -8
      |    8 2 6  8
      |____________
        8  2 6 8  0
    y = (x-1)(8*x**3 + 2*x**2 + 6*x + 8)
    '''
    #Build coff matrix 
    lastOutput = float(polynomial[0])
    output = []
    output.append(lastOutput)
    for i in range(1,len(polynomial) - 1):
        outputCurrent = polynomial[i]
        outputCurrent +=  lastOutput * root
        lastOutput = outputCurrent
        output.append(outputCurrent)
    #print(output)

    #check reminder is eaqual to zero
    if(len(output)-1 == 0):
        output(pop)
    return(output)

def buildPolynomialCoff(poly):
    #y= '8*x**4 - 6*x**3 + 4*x**2 + 2 * x**2 -8' 
    polyNoMinus = poly.replace('-', '+(-1)*')
    coff = 0
    exp = -1

    exprList = polyNoMinus.split('+')

    coffList = []
    coffDict = {}
    for expr  in exprList:
        expr = expr.strip()
        expr = expr.replace(' ',"")
        expr = expr.replace('**',"")
        xpos = expr.find('x')
        if (xpos > 0): 
            coff = expr[0:xpos-1]
            coff = eval(coff)
            if((len(expr)-xpos) > 1) :
                exp = expr[xpos+1:len(expr)]                
            elif((len(expr)-xpos) == 1) :
                exp = '1'
            if (exp.isdigit()):
                coffDict[int(exp)]= coff
        elif(xpos == 0): 
            if((len(expr)-xpos) > 1 ):
                exp = expr[xpos+1,len(expr)]
            elif((len(expr)-xpos) == 1) :
                exp = '1'
            if (exp.isdigit()):
                coffDict[int(exp)]= float(1.0)
        else:
            # May be constant 
            const = eval(expr)
            exp = 0
            if (const != 0):
                coffDict[int(exp)]= float(const)

    maxKey = 0
    for key in coffDict:
        maxKey = max(key,maxKey)
    
    #Add zero values to missing keys 
    #All degrees of exponents should exist 
    for key in range(maxKey+1):
        if( key in coffDict): continue
        else: coffDict[key] = 0

    coffDict = sorted(coffDict.items(),reverse = True)
    
    return [ coffDict[i][1] for i in range(len(coffDict)) ]

'''
print(buildPolynomialCoff('8*x**4 - 6*x**3 + 4*x**2 + 2 * x -8'))
print(buildPolynomialCoff('6 *x**4-2*x**3+5*x**2 -10'))


t = 1.2
#expr = eval('sin(4*t)')
#print('expr',expr)

y = '5*sin(4*x-1)'
r= roots(y)
print('root =', r(1))
'''
y = '5*sin(x) + 6*cos(x)'
r = roots(y)
print('Roots of ', str(r) , r(10))
'''
y = '2*(2*x+1)**3 +1'
r = roots(y)
print('Roots of', str(r) , r(-1))

y = '-2*(3*x-1)**7 -8'
r = roots(y)
print('Roots of', str(r), r(-1))

y = '3*  sin(x) - 1'
r = roots(y)
print('Roots of ', str(r), r(1))

y = '2 *x + 1'
r = roots(y)
print('Roots of ', str(r), r(1))

y= '8*x**4 - 6*x**3 + 4*x**2 + 2 * x -8'  #'6 *x**4-2*x**3+5*x**2+x -10'
r = roots(y)
print('Roots of ', str(r), r(1))
polynomial = [8,-6,4, 2, -8 ]#[6,-2,5,1,-10]
ldr = longDivision(polynomial,float(r(1)))
print('Roots of ', str(r), r(1), ldr)

print('rationalRootTesting = ',rationalRoot(polynomial))


y='6 *x**4-2*x**3+5*x**2+x -10'
r = roots(y)
print('Roots of ', str(r), r(1))
polynomial = [6,-2,5,1,-10]
ldr = longDivision(polynomial,float(r(1)))
print('Roots of ', str(r), r(1), ldr)
print('rationalRootTesting = ',rationalRoot(polynomial))

y = 'x**2-5*x +6'
r = roots(y)
print('Roots of ', str(r), r(1))
polynomial = [1,-5,6]
ldr = longDivision(polynomial,float(r(1)))
print('Roots of ', str(r), r(1), ldr)
print('rationalRootTesting = ',rationalRoot(polynomial))

y= '2*x**3 +1'
r = roots(y)
print('Roots of ', str(r), r(1))


y= '2*(2*x+1)**3 +1'
r = roots(y)
print('Roots of ', str(r), r(1))

y= '-2*(3*x-1)**7 -8'
r = roots(y)
print('Roots of ', str(r), r(1))

y = 'sin(x)'
r = roots(y)
print('Roots of ', str(r), r(1))

y = '3*  sin(4*x+2) -5'
r = roots(y)
print('Roots of ', str(r), r(1))

y = 'cos(x)'
r = roots(y)
print('Roots of ', str(r), r(1))


y = '3*  cos(4*x-2) +8'
r = roots(y)
print('Roots of ', str(r), r(1))

y = 'ln(x)'
r = roots(y)
print('Roots of ', str(r), r(1))'''

