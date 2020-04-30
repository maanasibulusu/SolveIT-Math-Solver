import math
import copy

#http://www.cs.cmu.edu/~112/schedule.html
def almostEqual(d1, d2, epsilon=10**-3):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1)) < epsilon

class Asymptotes(object):
    
    def __init__(self,function):
        self.function = function
        self.testfunction = function

    def hasDenom(self):
        for x in range(len(self.function)):
            if self.function[x] == '/':
                if self.function[x-2] != '(':
                    return True
        return False

    def functionDenom(self):
        if self.hasDenom ()== True:
            elemNum = self.function.index('/')
            self.testfunction = self.function
            length = len(self.testfunction)
            tester = self.testfunction
            if ')' == tester[elemNum+2]:
                tester = tester[elemNum:].replace(')','!',1)
                newtester = self.testfunction[:elemNum] + tester
                findNum = newtester.index('!')
                if '(' == self.testfunction[findNum+2]:
                    tester2 = self.testfunction[findNum+2:]
                    if tester2.startswith('('):
                        tester2 = tester2[1:]
                    if tester2.endswith(')'):
                        tester2 = tester2[:-1]
                    #print (tester2)
                    return tester2  
            else:
                tester = self.testfunction[elemNum+2:] 
                if tester.startswith('('):
                    tester = tester[1:]
                if tester.endswith(')'):
                    tester = tester[:-1]
                #print (tester)
                return tester
    
    def solveDenom(self):
        solveVA = []
        VADenom = []
        VA2Denom = 'Vertical Asymptotes:'
        x = -100
        while x<100:
            if (almostEqual(eval(self.functionDenom()),0)):
                solveVA.append((x))
            x += 0.001
        for elem in range(len(solveVA)):
            elemr = round(solveVA[elem],1)
            if elemr not in VADenom:
                VADenom.append(elemr)
        for elem in VADenom:
            VA2Denom += str(elem)
        return (VA2Denom)

    def hasE(self):
        if 'exp' in self.function or 'e' in self.function:
            return True
        else:
            return False

    def overallAsymptotes(self):
        oAsymptotes = ''
        if self.hasDenom() == True:
            oAsymptotes += (str(self.solveDenom()))
        if self.hasDenom() == False:
            oAsymptotes += ('No Vertical Asymptotes')
        return oAsymptotes + ','


a = Asymptotes('(x**2)/(x**3+1)')
print(a.overallAsymptotes())
