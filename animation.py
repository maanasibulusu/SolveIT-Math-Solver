from cmu_112_graphics import *
import random, math
from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
import derviative_integral as di
from derviative_integral import *
from rootstesting import roots 
import asymptote as asp
from asymptote import *
from asymptote1 import *
from rangefinal import *

#http://www.cs.cmu.edu/~112/schedule.html
def almostEqual(d1, d2, epsilon=10**-5):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1)) < epsilon

#http://www.cs.cmu.edu/~112/notes/notes-strings.html
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

#http://www.cs.cmu.edu/~112/notes/notes-strings.html
def writeFile(path, contents, perm = 'a'):
    with open(path, perm) as f:
        f.write(contents)

class Display(App):

    def appStarted(self):
        self.differStates = ['Home', 'Solver', 'Graph']
        self.currentState = self.differStates[0]
        #Below two lines of code inspired from https://effbot.org/tkinterbook/photoimage.htm
        image = Image.open("solveIT.png")
        #SolveIt image made from https://www.logomaker.com/ gud logo making website
        self.homeImage = ImageTk.PhotoImage(image)
        self.graphImage = None
        self.newgraphImage = None
        self.graphP1 = False
        self.graphP2 = False
        self.graphP3 = False
        self.graphP4 = False
        self.graphP5 = False
        self.graphP6 = False
        self.graphP7 = False
        self.graphP8 = False
        self.graphP9 = False
        self.graphP10 = False
        self.graphImage1 = None
        self.yList = []
        self.storeDEquation = []
        self.equation = ''
        self.cEquation =''
        self.submit = False
        self.equationEval = ''
        self.inputEquation = False
        self.storeEquation = []
        self.name = ''
        self.newUser = False
        self.storeNewUser = []
        self.invalid = False
        self.derivative = ''
        self.firstderivative = ''
        self.secondderivative = ''
        self.graphDerivative = False
        self.graphIntegral = False
        self.integral = ''
        self.domain = ''
        self.range = ''
        self.roots = ''
        self.asymptotes = ''
        self.graph = ''
        self.npEquation = ''
        self.newEquation = ''
        self.np1Equation = ''
        self.np2Equation = ''
        self.sDE1 = ''
        self.sDE2 = ''
        self.sDE3 = ''
        self.sDE4 = ''
        self.sDE5 = ''
        self.sDE6 = ''
        self.sDE7 = ''
        self.sDE8 = ''
        self.sDE9 = ''
        self.sDE10 = ''
        self.detailEquation = ''
        self.sub = False
        self.sub1 = False
        self.sub2 = False
        self.xer = 0
        self.xer1 = 0
        self.xer2 = 0
        self.yer = 100
        self.yer1 = 100
        self.yer2 = 100
        self.secderivative1 = ''
        self.secderivative2 = ''
        self.firstderivative1 = ''
        self.firstderivative2 = ''
        self.derivative1 = ''
        self.derivative2 = ''
        self.lensub2 = False
        self.lensub1 = False
        self.lensub = False
        self.subI = False
        self.lensubI = False
        self.xerI = 0
        self.yerI = 70
        self.modIntegral1 = ''
        self.modIntegral2 = ''
        self.subD = False
        self.lensubD = False
        self.subR = False
        self.lensubR = False
        self.subRo = False
        self.lensubRo = False
        self.xerD = 0
        self.yerD = 18
        self.xerR = 0
        self.yerR = 18
        self.xerRo = 0
        self.yerRo = 18
        self.modDomain1 = ''
        self.modDomain2 = ''
        self.modRange1 = ''
        self.modRange2 = ''
        self.modRoots1 = ''
        self.modRoots2 = ''
        self.subA = False
        self.lensubA = False
        self.xerA = 0
        self.yerA = 70
        self.modAsy1 = ''
        self.modAsy2 = ''
        
    def mousePressed(self,event):
        if self.currentState == 'Home':
            self.homeMousePressed(event)
        if self.currentState == 'Solver':
            self.solverMousePressed(event)
        if self.currentState == 'Graph':
            self.graphMousePressed(event)
    
    def keyPressed(self,event):
        if self.currentState == 'Home':
            if self.inputEquation == True:
                self.inputEquationKeyPressed(event)
            if self.newUser == True:
                self.inputNameKeyPressed(event)
        if self.currentState == 'Solver':
            if self.sub == True or self.sub1 == True or self.sub2 == True or self.subI == True or self.subD == True or self.subR == True or self.subRo == True or self.lensubA == True:
                self.solverKeyPressed(event)
    
    def redrawAll(self,canvas):
        if self.currentState == 'Home':
            self.homeScreenRedrawAll(canvas)
        if self.currentState == 'Solver':
            self.solverRedrawAll(canvas)
        if self.currentState == 'Graph':
            self.graphRedrawAll(canvas)

#Home Screen Menu
    def homeMousePressed(self,event):
        mouseX = event.x
        mouseY = event.y
        
        #Enter Name
        if event.x > 220 and event.x < 750 and event.y > 330 and event.y < 370:
            self.newUser = True
        
        #Submit Button for Name
        if event.x > 420 and event.x < 550 and event.y > 380 and event.y < 410:
            self.newUser = False
            self.storeNewUser.append(self.name)
            userfile = self.name + '.txt'
            if userfile in os.listdir('users'):
                path = 'users/'+ self.name + '.txt'
                fileReader = (readFile(path))
                lines = fileReader.split('\n')
                if len(lines) > 9:
                    tenners = lines[(len(lines)-11):len(lines)]
                else:
                    tenners = lines
                for elem in tenners:
                    elem += '\n'
                    self.storeDEquation.append(elem) 
            else:
                path = 'users/'+ self.name + '.txt'
                open(path,'w+')
                self.storeDEquation = []

        #Enter Equation
        if event.x > 220 and event.x < 750 and event.y > 470 and event.y < 510:
            self.inputEquation = True
            self.cEquation = ''

        #Submit Button for Equation
        if event.x > 420 and event.x < 550 and event.y > 520 and event.y < 550:
            if self.invalid == False:
                self.inputEquation = False
                self.storeEquation.append(self.equation)
                x = di.Basic('x')
                y = eval(self.cEquation)
                if type(y) == int or type(y) == float:
                    self.derivative = ''
                    self.integral = di.Basic(x) * y
                    self.firstderivative = ''
                    self.secondderivative = ''
                else:
                    self.integral = y.integrate().simplify().simplify().toString()
                    self.derivative = y.derivative().simplify().simplify().toString()
                    self.firstderivative = y.derivative().derivative().simplify().simplify().toString()
                    self.secondderivative = y.derivative().derivative().derivative().simplify().simplify().toString()
                if len(str(self.secondderivative)) > 100:
                    self.lensub2 = True
                    self.secderivative1 = str(self.secondderivative)[0:100]
                if len(str(self.firstderivative)) > 100:
                    self.lensub1 = True
                    self.firstderivative1 = str(self.firstderivative)[0:100]
                if len(str(self.derivative)) > 100:
                    self.lensub = True
                    self.derivative1 = str(self.derivative)[0:100]
                if len(str(self.integral)) > 70:
                    self.lensubI = True
                    self.modIntegral1 = str(self.integral)[0:70]
                if len(str(self.domain)) > 18:
                    self.lensubD = True
                    self.modDomain1 = str(self.domain)[0:18]
                if len(str(self.range)) > 18:
                    self.lensubR = True
                    self.modRange1 = str(self.range)[0:18]
                if len(str(self.roots)) > 18:
                    self.lensubRo = True
                    self.modRoots1 = str(self.roots)[0:18]
                if len(str(self.asymptotes)) > 70:
                    self.lensubA = True
                    self.modAsy1 = str(self.asymptotes)[0:70]
                self.domain = str(y.domain())
                asymp = asp.Asymptotes(self.cEquation)
                horizontalAsy = Asymptote(y)
                self.asymptotes = str(asymp.overallAsymptotes()) + str(horizontalAsy.HorAsymptote())
                root1 = roots(self.cEquation)
                self.roots = root1(1)
                ranger = RangeTesting(y)
                self.range = ranger.rangeF()
                path = 'users/'+ self.name + '.txt'
                newline = str(self.equation) + '\n'
                writeFile(path, newline)
                self.storeDEquation.append(newline)
                if (len(self.storeDEquation) > 9):
                    self.storeDEquation.pop(0)
                self.equation = ''
                self.submit = True
                x1 =-np.pi
                x2 = np.pi
                x = np.linspace(x1,x2,100)
                self.npEquation = self.cEquation
                self.np1Equation = (self.derivative)
                self.np2Equation = (self.integral)
                if 'sin' in self.cEquation:
                    self.npEquation = self.npEquation.replace('sin','np.sin')
                if 'sin' in str(self.derivative):
                    self.np1Equation = self.np1Equation.replace('sin','np.sin')
                if 'sin' in str(self.integral):
                    self.np2Equation = self.np2Equation.replace('sin','np.sin')
                if 'cos' in self.cEquation:
                    self.npEquation = self.npEquation.replace('cos','np.cos')
                if 'cos' in str(self.derivative):
                    self.np1Equation = self.np1Equation.replace('cos','np.cos')
                if 'cos' in str(self.integral):
                    self.np2Equation = self.np2Equation.replace('cos','np.cos')
                if 'tan' in self.cEquation:
                    self.npEquation = self.npEquation.replace('tan','np.tan')
                if 'tan' in str(self.derivative):
                    self.np1Equation = self.np1Equation.replace('tan','np.tan')
                if 'tan' in str(self.integral):
                    self.np2Equation = self.np2Equation.replace('tan','np.tan')
                if 'exp' in self.cEquation:
                    self.npEquation = self.npEquation.replace('exp','np.exp')
                if 'exp' in str(self.derivative):
                    self.np1Equation = self.np1Equation.replace('exp','np.exp')
                if 'exp' in str(self.integral):
                    self.np2Equation = self.np2Equation.replace('exp','np.exp')
                if 'ln' in self.cEquation:
                    self.npEquation = self.npEquation.replace('ln','np.log')
                if 'ln' in str(self.derivative):
                    self.np1Equation = self.np1Equation.replace('ln','np.log')
                if 'ln' in str(self.integral):
                    self.np2Equation = self.np2Equation.replace('ln','np.log')
                if self.cEquation != '':
                    y = np.array(eval(self.npEquation))
                if type(self.derivative) != Constant and type(self.derivative) != int and type(self.derivative) != float:
                    b = np.array(eval(self.np1Equation))
                if self.integral != '' and type(self.integral) != int and type(self.integral) != float and self.integral != '0':
                    d = np.array(eval(self.np2Equation))
                fig = plt.figure(figsize = (4,3))
                ax = fig.add_subplot(1, 1, 1)
                #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
                ax.spines['left'].set_position('center')
                ax.spines['bottom'].set_position('center')
                ax.spines['right'].set_color('none')
                ax.spines['top'].set_color('none')
                ax.xaxis.set_ticks_position('bottom')
                ax.yaxis.set_ticks_position('left')
                if self.cEquation != '':
                    plt.plot(x,y, 'b', label='y='+self.cEquation)
                if type(self.derivative) != Constant and type(self.derivative) != int and type(self.derivative) != float:
                    plt.plot(x,b, 'r', label='derivative')
                if self.integral != '' and type(self.integral) != int and type(self.integral) != float and self.integral != '0':
                    plt.plot(x,d, 'g', label='integral')
                plt.legend(loc='upper left')
                self.newEquation = self.cEquation
                if '/' in self.cEquation:
                    self.newEquation = self.cEquation.replace('/','')
                self.detailEquation = self.newEquation
                plt.savefig('graphs/' + self.newEquation + '.png', bbox_inches='tight')
                image2 = Image.open("graphs/" + self.newEquation + ".png")
                self.graphImage = ImageTk.PhotoImage(image2)
                #https://matplotlib.org/tutorials/introductory/pyplot.html
        
        #Go to Calculator Button
        if event.x > 400 and event.x < 900 and event.y > 610 and event.y < 750:
            self.currentState = self.differStates[1]
            self.cEquation = ''
            if self.storeDEquation != '':
                self.sDE1 = self.storeDEquation[0]
            else:
                self.sDE1 = ''
            if len(self.storeDEquation) > 1:
                self.sDE2 = self.storeDEquation[1]
            else:
                self.sDE2 = ''
            if len(self.storeDEquation) > 2:
                self.sDE3 = self.storeDEquation[2]
            else:
                self.sDE3 = ''
            if len(self.storeDEquation) > 3:
                self.sDE4 = self.storeDEquation[3]
            else:
                self.sDE4 = ''
            if len(self.storeDEquation) > 4:
                self.sDE5 = self.storeDEquation[4]
            else:
                self.sDE5 = ''
            if len(self.storeDEquation) > 5:
                self.sDE6 = self.storeDEquation[5]
            else:
                self.sDE6 = ''
            if len(self.storeDEquation) > 6:
                self.sDE7 = self.storeDEquation[6]
            else:
                self.sDE7 = ''
            if len(self.storeDEquation) > 7:
                self.sDE8 = self.storeDEquation[7]
            else:
                self.sDE8 = ''
            if len(self.storeDEquation) > 8:
                self.sDE9 = self.storeDEquation[8]
            else:
                self.sDE9 = ''
            if len(self.storeDEquation) > 9:
                self.sDE10 = self.storeDEquation[9]
            else:
                self.sDE10 = ''

        
        #Calculator Functions
        #1st Row
        if event.x > 1100 and event.x < 1150 and event.y > 270 and event.y < 320:
            self.inputEquation = True
            self.equation += 'sin'
            self.cEquation = self.equation
            self.equationEval += 'math.sin'
        
        #2nd Row
        if event.x > 800 and event.x < 900 and event.y > 320 and event.y < 370:
            self.inputEquation = True
            self.equation += 'x'
            self.cEquation = self.equation
        
        if event.x > 900 and event.x < 950 and event.y > 320 and event.y < 370:
            self.inputEquation = True
            self.equation += '.'
            self.cEquation = self.equation
            self.equationEval += '.'
        
        if event.x > 950 and event.x < 1000 and event.y > 320 and event.y < 370:
            self.inputEquation = True
            self.equation += '+'
            self.cEquation = self.equation
            self.equationEval += '+'
        
        if event.x > 1000 and event.x < 1050 and event.y > 320 and event.y < 370:
            self.inputEquation = True
            self.equation += '**'
            self.cEquation = self.equation
            self.equationEval += '**'
        
        if event.x > 1050 and event.x < 1100 and event.y > 320 and event.y < 370:
            self.inputEquation = True
            self.equation += '**2'
            self.cEquation = self.equation
            self.equationEval += '**2'
        
        if event.x > 1100 and event.x < 1150 and event.y > 320 and event.y < 370:
            self.inputEquation = True
            self.equation += 'cos'
            self.cEquation = self.equation
            self.equationEval += 'math.cos'
        
        #3rd Row
        if event.x > 800 and event.x < 850 and event.y > 370 and event.y < 420:
            self.inputEquation = True
            self.equation += '7'
            self.cEquation = self.equation
            self.equationEval += '7'
        
        if event.x > 850 and event.x < 900 and event.y > 370 and event.y < 420:
            self.inputEquation = True
            self.equation += '8'
            self.cEquation = self.equation
            self.equationEval += '8'
        
        if event.x > 900 and event.x < 950 and event.y > 370 and event.y < 420:
            self.inputEquation = True
            self.equation += '9'
            self.cEquation = self.equation
            self.equationEval += '9'
        
        if event.x > 950 and event.x < 1000 and event.y > 370 and event.y < 420:
            self.inputEquation = True
            self.equation += '-'
            self.cEquation = self.equation
            self.equationEval += '-'
        
        if event.x > 1000 and event.x < 1050 and event.y > 370 and event.y < 420:
            self.inputEquation = True
            self.equation += '/'
            self.cEquation = self.equation
            self.equationEval += '/'
        
        if event.x > 1050 and event.x < 1100 and event.y > 370 and event.y < 420:
            self.inputEquation = True
            self.equation += '**3'
            self.cEquation = self.equation
            self.equationEval += '**3'
        
        if event.x > 1100 and event.x < 1150 and event.y > 370 and event.y < 420:
            self.inputEquation = True
            self.equation += 'tan'
            self.cEquation = self.equation
            self.equationEval += 'math.tan'
        
        #4th Row
        if event.x > 800 and event.x < 850 and event.y > 420 and event.y < 470:
            self.inputEquation = True
            self.equation += '4'
            self.cEquation = self.equation
            self.equationEval += '4'
        
        if event.x > 850 and event.x < 900 and event.y > 420 and event.y < 470:
            self.inputEquation = True
            self.equation += '5'
            self.cEquation = self.equation
            self.equationEval += '5'
        
        if event.x > 900 and event.x < 950 and event.y > 420 and event.y < 470:
            self.inputEquation = True
            self.equation += '6'
            self.cEquation = self.equation
            self.equationEval += '6'
        
        if event.x > 950 and event.x < 1000 and event.y > 420 and event.y < 470:
            self.inputEquation = True
            self.equation += '*'
            self.cEquation = self.equation
            self.equationEval += '*'
        
        if event.x > 1000 and event.x < 1050 and event.y > 420 and event.y < 470:
            self.inputEquation = True
            self.equation += 'exp'
            self.cEquation = self.equation
            self.equationEval += 'math.exp'
        
        if event.x > 1050 and event.x < 1100 and event.y > 420 and event.y < 470:
            self.inputEquation = True
            self.equation += 'ln'
            self.cEquation = self.equation
            self.equationEval += 'math.log'
        
        if event.x > 1100 and event.x < 1150 and event.y > 420 and event.y < 470:
            self.inputEquation = True
            self.equation += 'sec'
            self.cEquation = self.equation
            self.equationEval += '(1/math.cos)'
        
        #5th Row
        if event.x > 800 and event.x < 850 and event.y > 470 and event.y < 520:
            self.inputEquation = True
            self.equation += '1'
            self.cEquation = self.equation
            self.equationEval += '1'
        
        if event.x > 850 and event.x < 900 and event.y > 470 and event.y < 520:
            self.inputEquation = True
            self.equation += '2'
            self.cEquation = self.equation
            self.equationEval += '2'
        
        if event.x > 900 and event.x < 950 and event.y > 470 and event.y < 520:
            self.inputEquation = True
            self.equation += '3'
            self.cEquation = self.equation
            self.equationEval += '3'
        
        if event.x > 950 and event.x < 1000 and event.y > 470 and event.y < 520:
            self.inputEquation = True
            self.equation += ' '
            self.cEquation = self.equation
            self.equationEval += ' '
        
        if event.x > 1000 and event.x < 1100 and event.y > 470 and event.y < 520:
            self.inputEquation = True
            self.equation = self.equation[:-1]
            self.cEquation = self.equation
            self.equationEval = self.equation[:-1]

        if event.x > 1100 and event.x < 1150 and event.y > 470 and event.y < 520:
            self.inputEquation = True
            self.equation += '**(1/2)'
            self.cEquation = self.equation
            self.equationEval += '**(1/2)'

        #6th Row
        if event.x > 800 and event.x < 850 and event.y > 520 and event.y < 570:
            self.inputEquation = True
            self.equation += '0'
            self.cEquation = self.equation
            self.equationEval += '0'
        
        if event.x > 850 and event.x < 950 and event.y > 520 and event.y < 570:
            self.inputEquation = True
            self.equation = ''
            self.cEquation = self.equation
            self.equationEval = ''
        
        if event.x > 950 and event.x < 1050 and event.y > 520 and event.y < 570:
            self.inputEquation = True
            #try and except code learned and inspired from https://www.w3schools.com/python/python_try_except.asp
            try:
                self.equation = str(eval(self.equationEval))
                self.equationEval = self.equation
                self.cEquation = self.equation
            except:
                self.equation += '   Value is Invalid'
                self.cEquation = self.equation
        
        if event.x > 1050 and event.x < 1100 and event.y > 520 and event.y < 570:
            self.inputEquation = True
            self.equation += '('
            self.cEquation = self.equation
            self.equationEval += '('
        
        if event.x > 1100 and event.x < 1150 and event.y > 520 and event.y < 570:
            self.inputEquation = True
            self.equation += ')'
            self.cEquation = self.equation
            self.equationEval += ')'

        #Submit Button for Calculator
        if event.x > 925 and event.x < 1035 and event.y > 590 and event.y < 620:
            if self.invalid == False:
                self.inputEquation = False
                self.storeEquation.append(self.equation)
                x = di.Basic('x')
                y = eval(self.cEquation)
                if type(y) == int or type(y) == float:
                    self.derivative = ''
                    self.integral = di.Basic(x) * y
                    self.firstderivative = ''
                    self.secondderivative = ''
                else:
                    self.integral = y.integrate().simplify().simplify().toString()
                    self.derivative = y.derivative().simplify().simplify().toString()
                    self.firstderivative = y.derivative().derivative().simplify().simplify().toString()
                    self.secondderivative = y.derivative().derivative().derivative().simplify().simplify().toString()
                if len(str(self.secondderivative)) > 100:
                    self.lensub2 = True
                    self.secderivative1 = str(self.secondderivative)[0:100]
                if len(str(self.firstderivative)) > 100:
                    self.lensub1 = True
                    self.firstderivative1 = str(self.firstderivative)[0:100]
                if len(str(self.derivative)) > 100:
                    self.lensub = True
                    self.derivative1 = str(self.derivative)[0:100]
                if len(str(self.integral)) > 70:
                    self.lensubI = True
                    self.modIntegral1 = str(self.integral)[0:70]
                if len(str(self.domain)) > 18:
                    self.lensubD = True
                    self.modDomain1 = str(self.domain)[0:18]
                if len(str(self.range)) > 18:
                    self.lensubR = True
                    self.modRange1 = str(self.range)[0:18]
                if len(str(self.roots)) > 18:
                    self.lensubRo = True
                    self.modRoots1 = str(self.roots)[0:18]
                if len(str(self.asymptotes)) > 70:
                    self.lensubA = True
                    self.modAsy1 = str(self.asymptotes)[0:70]
                self.domain = str(y.domain())
                asymp = asp.Asymptotes(self.cEquation)
                horizontalAsy = Asymptote(y)
                self.asymptotes = str(asymp.overallAsymptotes()) + str(horizontalAsy.HorAsymptote())
                root1 = roots(self.cEquation)
                self.roots = root1(1)
                ranger = RangeTesting(y)
                self.range = ranger.rangeF()
                path = 'users/'+ self.name + '.txt'
                newline = str(self.equation) + '\n'
                writeFile(path, newline)
                self.storeDEquation.append(newline)
                if (len(self.storeDEquation) > 9):
                    self.storeDEquation.pop(0)
                self.equation = ''
                self.submit = True
                x1 =-np.pi
                x2 = np.pi
                x = np.linspace(x1,x2,100)
                self.npEquation = self.cEquation
                self.np1Equation = str(self.derivative)
                self.np2Equation = str(self.integral)
                if 'sin' in self.cEquation:
                    self.npEquation = self.npEquation.replace('sin','np.sin')
                if 'sin' in str(self.derivative):
                    self.np1Equation = self.np1Equation.replace('sin','np.sin')
                if 'sin' in str(self.integral):
                    self.np2Equation = self.np2Equation.replace('sin','np.sin')
                if 'cos' in self.cEquation:
                    self.npEquation = self.npEquation.replace('cos','np.cos')
                if 'cos' in str(self.derivative):
                    self.np1Equation = self.np1Equation.replace('cos','np.cos')
                if 'cos' in str(self.integral):
                    self.np2Equation = self.np2Equation.replace('cos','np.cos')
                if 'tan' in self.cEquation:
                    self.npEquation = self.npEquation.replace('tan','np.tan')
                if 'tan' in str(self.derivative):
                    self.np1Equation = self.np1Equation.replace('tan','np.tan')
                if 'tan' in str(self.integral):
                    self.np2Equation = self.np2Equation.replace('tan','np.tan')
                if 'exp' in self.cEquation:
                    self.npEquation = self.npEquation.replace('exp','np.exp')
                if 'exp' in str(self.derivative):
                    self.np1Equation = self.np1Equation.replace('exp','np.exp')
                if 'exp' in str(self.integral):
                    self.np2Equation = self.np2Equation.replace('exp','np.exp')
                if 'ln' in self.cEquation:
                    self.npEquation = self.npEquation.replace('ln','np.log')
                if 'ln' in str(self.derivative):
                    self.np1Equation = self.np1Equation.replace('ln','np.log')
                if 'ln' in str(self.integral):
                    self.np2Equation = self.np2Equation.replace('ln','np.log')
                if self.cEquation != '':
                    y = np.array(eval(self.npEquation))
                if self.derivative != '' and type(self.derivative) != int and type(self.derivative) != float:
                    b = np.array(eval(self.np1Equation))
                if self.integral != '' and type(self.integral) != int and type(self.integral) != float:
                    d = np.array(eval(self.np2Equation))
                fig = plt.figure(figsize = (4,3))
                ax = fig.add_subplot(1, 1, 1)
                #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
                ax.spines['left'].set_position('center')
                ax.spines['bottom'].set_position('center')
                ax.spines['right'].set_color('none')
                ax.spines['top'].set_color('none')
                ax.xaxis.set_ticks_position('bottom')
                ax.yaxis.set_ticks_position('left')
                if self.cEquation != '':
                    plt.plot(x,y, 'b', label='y='+self.cEquation)
                if type(self.derivative) != Constant and type(self.derivative) != int and type(self.derivative) != float:
                    plt.plot(x,b, 'r', label='derivative')
                if self.integral != '' and type(self.integral) != int and type(self.integral) != float and self.integral != '0':
                    plt.plot(x,d, 'g', label='integral')
                plt.legend(loc='upper left')
                self.newEquation = self.cEquation
                if '/' in self.cEquation:
                    self.newEquation = self.cEquation.replace('/','')
                self.detailEquation = self.newEquation
                plt.savefig('graphs/' + self.newEquation + '.png', bbox_inches='tight')
                image2 = Image.open("graphs/" + self.newEquation + ".png")
                self.graphImage = ImageTk.PhotoImage(image2)
                #https://matplotlib.org/tutorials/introductory/pyplot.html

    def inputEquationKeyPressed(self,event):
        if self.inputEquation == True:
            if event.key == 'Space':
                self.equation += ' '
                self.cEquation += ' '
            elif event.key == 'Delete':
                self.equation = self.equation[:-1]
                self.cEquation = self.cEquation[:-1]
            else:
                self.equation += event.key
                self.cEquation += event.key

    def inputNameKeyPressed(self,event):
        if self.newUser == True:
            if event.key == 'Space':
                self.name += "  "
            elif event.key == 'Delete':
                self.name = self.name[:-1]
            else:
                self.name += event.key

    def homeScreenRedrawAll(self,canvas):
        canvas.create_rectangle(0,0,self.width,self.height, fill ="#b2cecf",width = 0)
        canvas.create_text(600,200, text = 'An Easy Math Solver', font = 'Arial 28 bold')
        canvas.create_image(600,20, image=self.homeImage, anchor =N)
        canvas.create_rectangle(220,330,750,370,fill = "#b2cecf",outline ='dark blue')
        canvas.create_rectangle(420,380,550,410, fill = '#0e385f', outline = 'white')
        canvas.create_rectangle(220,470,750,510, fill = '#b2cecf', outline = 'dark blue')
        canvas.create_text(435,350, text = self.name, fill = 'black', font = 'Arial 16')
        canvas.create_rectangle(420,520,550,550, fill = '#0e385f', outline = 'white')
        canvas.create_text(435,490, text = self.equation, fill = 'black', font = 'Arial 16')
        canvas.create_rectangle(400,610,850,750, fill = '#0e385f', outline = 'white', width = 5)
        canvas.create_text(170,300,text = "Enter Name:", fill = 'black', font = "Arial 24 bold")
        canvas.create_text(482,395, text = 'Submit', fill = 'white', font = 'Arial 18 bold')
        canvas.create_text(180,440, text = 'Enter Equation:', fill = 'black', font = 'Arial 24 bold')
        if self.invalid == True:
            canvas.create_text(250,380, text = 'Invalid', fill = 'red', font = 'Arial 14' )
        canvas.create_text(482,535, text = 'Submit', fill = 'White', font = 'Arial 18 bold')
        canvas.create_rectangle(925,590,1035,620, fill = '#0e385f', outline = 'white' )
        canvas.create_text(980,605, text = 'Submit', fill = 'white', font = 'Arial 18 bold')
        canvas.create_text(625,680, text = 'Lets SolveIT', fill = 'white', font = 'Arial 56 bold' )
        
        #Calculator Drawing
        canvas.create_rectangle(800,270,1150,570, fill = '#b2cecf', outline = '#0e385f', width = 10)
        #First Row 
        canvas.create_rectangle(800,270,1100,320, fill = '#b2cecf', outline = 'white')
        canvas.create_text(950,295, text = self.equation, fill = 'black', font = 'Arial 18 bold')
        canvas.create_rectangle(1100,270,1150,320, fill = '#0e385f', outline = 'white')
        canvas.create_text(1125,295, text = 'sin', fill = 'white', font = 'Arial 18 bold' )
        #2nd Row
        canvas.create_rectangle(800,320,900,370, fill = '#0e385f', outline = 'white')
        canvas.create_text(850,345, text = 'X', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(900,320,950,370, fill = '#0e385f', outline = 'white')
        canvas.create_text(925,345, text = '.', fill = 'white', font = 'Arial 24 bold' )
        canvas.create_rectangle(950,320,1000,370, fill = '#0e385f', outline = 'white')
        canvas.create_text(975,345, text = '+', fill = 'white', font = 'Arial 24 bold' )
        canvas.create_rectangle(1000,320,1050,370, fill = '#0e385f', outline = 'white')
        canvas.create_text(1025,345, text = '^', fill = 'white', font = 'Arial 24 bold' )
        canvas.create_rectangle(1050,320,1100,370, fill = '#0e385f', outline = 'white')
        canvas.create_text(1075,345, text = '^2', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(1100,320,1150,370, fill = '#0e385f', outline = 'white')
        canvas.create_text(1125,345, text = 'cos', fill = 'white', font = 'Arial 18 bold' )
        #3rd Row
        canvas.create_rectangle(800,370,850,420, fill = '#0e385f', outline = 'white')
        canvas.create_text(825,395, text = '7', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(850,370,900,420, fill = '#0e385f', outline = 'white')
        canvas.create_text(875,395, text = '8', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(900,370,950,420, fill = '#0e385f', outline = 'white')
        canvas.create_text(925,395, text = '9', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(950,370,1000,420, fill = '#0e385f', outline = 'white')
        canvas.create_text(975,395, text = '-', fill = 'white', font = 'Arial 24 bold' )
        canvas.create_rectangle(1000,370,1050,420, fill = '#0e385f', outline = 'white')
        canvas.create_text(1025,395, text = '/', fill = 'white', font = 'Arial 24 bold' )
        canvas.create_rectangle(1050,370,1100,420, fill = '#0e385f', outline = 'white')
        canvas.create_text(1075,395, text = '^3', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(1100,370,1150,420, fill = '#0e385f', outline = 'white')
        canvas.create_text(1125,395, text = 'tan', fill = 'white', font = 'Arial 18 bold' )
        #4th Row
        canvas.create_rectangle(800,420,850,470, fill = '#0e385f', outline = 'white')
        canvas.create_text(825,445, text = '4', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(850,420,900,470, fill = '#0e385f', outline = 'white')
        canvas.create_text(875,445, text = '5', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(900,420,950,470, fill = '#0e385f', outline = 'white')
        canvas.create_text(925,445, text = '6', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(950,420,1000,470, fill = '#0e385f', outline = 'white')
        canvas.create_text(975,445, text = '*', fill = 'white', font = 'Arial 24 bold' )
        canvas.create_rectangle(1000,420,1050,470, fill = '#0e385f', outline = 'white')
        canvas.create_text(1025,445, text = 'e', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(1050,420,1100,470, fill = '#0e385f', outline = 'white')
        canvas.create_text(1075,445, text = 'ln', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(1100,420,1150,470, fill = '#0e385f', outline = 'white')
        canvas.create_text(1125,445, text = 'sec', fill = 'white', font = 'Arial 18 bold' )
        #5th Row
        canvas.create_rectangle(800,470,850,520, fill = '#0e385f', outline = 'white')
        canvas.create_text(825,495, text = '1', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(850,470,900,520, fill = '#0e385f', outline = 'white')
        canvas.create_text(875,495, text = '2', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(900,470,950,520, fill = '#0e385f', outline = 'white')
        canvas.create_text(925,495, text = '3', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(950,470,1000,520, fill = '#0e385f', outline = 'white')
        canvas.create_text(975,495, text = 'Space', fill = 'white', font = 'Arial 12 bold' )
        canvas.create_rectangle(1000,470,1100,520, fill = '#0e385f', outline = 'white')
        canvas.create_text(1050,495, text = 'Del', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(1100,470,1150,520, fill = '#0e385f', outline = 'white')
        canvas.create_text(1125,495, text = 'sqrt', fill = 'white', font = 'Arial 16 bold' )
        #6th Row
        canvas.create_rectangle(800,520,850,570, fill = '#0e385f', outline = 'white')
        canvas.create_text(825,545, text = '0', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(850,520,950,570, fill = '#0e385f', outline = 'white')
        canvas.create_text(900,545, text = 'AC', fill = 'white', font = 'Arial 24 bold' )
        canvas.create_rectangle(950,520,1050,570, fill = '#0e385f', outline = 'white')
        canvas.create_text(1000,545, text = '=', fill = 'white', font = 'Arial 24 bold' )
        canvas.create_rectangle(1050,520,1100,570, fill = '#0e385f', outline = 'white')
        canvas.create_text(1075,545, text = '(', fill = 'white', font = 'Arial 18 bold' )
        canvas.create_rectangle(1100,520,1150,570, fill = '#0e385f', outline = 'white')
        canvas.create_text(1125,545, text = ')', fill = 'white', font = 'Arial 18 bold' )

#Solver Menu
    def solverMousePressed(self,event):
        mouseX = event.x
        mouseY = event.y

        #Home Button
        if event.x > 40 and event.x < 180 and event.y > 30 and event.y < 100:
            self.currentState = self.differStates[0]
        
        #Clear All Button
        if event.x > 675 and event. x < 710 and event.y > 370 and event.y < 385:
            self.firstderivative = ''
            self.secondderivative = ''
            self.graphDerivative = False
        
        #Graph 1st derivative 
        if event.x > 600 and event.x < 780 and event.y > 280 and event.y < 320:
            #graph first derivative
            self.graphDerivative = True
        
        #Graph Second Derivative
        if event.x > 600 and event.x < 780 and event.y > 320 and event.y < 360:
            #graph second derivative 
            self.graphDerivative = True
        
        #Enter New Equation Button
        if event.x > 200 and event.x < 500 and event.y > 720 and event.y < 790:
            self.currentState = self.differStates[0]
            self.sub = False
            self.sub1 = False
            self.sub2 = False
            self.xer = 0
            self.xer1 = 0
            self.xer2 = 0
            self.yer = 100
            self.yer1 = 100
            self.yer2 = 100
            self.secderivative1 = ''
            self.secderivative2 = ''
            self.firstderivative1 = ''
            self.firstderivative2 = ''
            self.derivative1 = ''
            self.derivative2 = ''
            self.lensub2 = False
            self.lensub1 = False
            self.lensub = False
            self.subI = False
            self.lensubI = False
            self.xerI = 0
            self.yerI = 70
            self.modIntegral1 = ''
            self.modIntegral2 = ''
            self.subD = False
            self.lensubD = False
            self.subR = False
            self.lensubR = False
            self.subRo = False
            self.lensubRo = False
            self.xerD = 0
            self.yerD = 18
            self.xerR = 0
            self.yerR = 18
            self.xerRo = 0
            self.yerRo = 18
            self.modDomain1 = ''
            self.modDomain2 = ''
            self.modRange1 = ''
            self.modRange2 = ''
            self.modRoots1 = ''
            self.modRoots2 = ''
            self.subA = False
            self.lensubA = False
            self.xerA = 0
            self.yerA = 70
            self.modAsy1 = ''
            self.modAsy2 = ''

        #Detailed Graph Screen
        if event.x > 900 and event.x < 1050 and event.y > 740 and event.y < 770:
            self.currentState = self.differStates[2]
            self.submit = True
            if self.submit == True:
                if '/' in self.detailEquation:
                    self.detailEquation = self.detailEquation.replace('/','')
                image3 = Image.open("graphs/" + self.detailEquation + '.png')
                new_image = image3.resize((600, 500))
                new_image.save('graphs/' + self.detailEquation + 'resize.png')
                image4 = Image.open('graphs/' + self.detailEquation + 'resize.png')
                self.newgraphImage = ImageTk.PhotoImage(image4)       

        if event.x>950 and event.x<1150 and event.y>70 and event.y<101:
            self.graphP1 = True
            self.submit = False
            x1 =-np.pi
            x2 = np.pi
            x = np.linspace(x1,x2,100)
            self.npEquation = self.sDE1
            if 'sin' in self.sDE1:
                self.npEquation = self.npEquation.replace('sin','np.sin')
            if 'cos' in self.sDE1:
                self.npEquation = self.npEquation.replace('cos','np.cos')
            if 'tan' in self.sDE1:
                self.npEquation = self.npEquation.replace('tan','np.tan')
            if 'exp' in self.sDE1:
                self.npEquation = self.npEquation.replace('exp','np.exp')
            if 'ln' in self.sDE1:
                self.npEquation = self.npEquation.replace('ln','np.log')
            if self.sDE1 != '':
                y = eval(self.npEquation)
            fig = plt.figure(figsize = (4,3))
            ax = fig.add_subplot(1, 1, 1)
            #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            if self.sDE1 != '':
                plt.plot(x,y, 'b', label='y='+self.sDE1)
            plt.legend(loc='upper left')
            self.newEquation = self.sDE1
            if '/' in self.sDE1:
                self.newEquation = self.sDE1.replace('/','')
            plt.savefig('graphs/' + self.newEquation + 'new.png', bbox_inches='tight')
            image2 = Image.open("graphs/" + self.newEquation + "new.png")
            self.graphImage1 = ImageTk.PhotoImage(image2)
        #https://matplotlib.org/tutorials/introductory/pyplot.html

        if event.x>950 and event.x<1150 and event.y>101 and event.y<132:
            self.graphP2 = True
            self.submit = False
            x1 =-np.pi
            x2 = np.pi
            x = np.linspace(x1,x2,100)
            self.npEquation = self.sDE2
            if 'sin' in self.sDE2:
                self.npEquation = self.npEquation.replace('sin','np.sin')
            if 'cos' in self.sDE2:
                self.npEquation = self.npEquation.replace('cos','np.cos')
            if 'tan' in self.sDE2:
                self.npEquation = self.npEquation.replace('tan','np.tan')
            if 'exp' in self.sDE2:
                self.npEquation = self.npEquation.replace('exp','np.exp')
            if 'ln' in self.sDE2:
                self.npEquation = self.npEquation.replace('ln','np.log')
            if self.sDE2 != '':
                y = eval(self.npEquation)
            fig = plt.figure(figsize = (4,3))
            ax = fig.add_subplot(1, 1, 1)
            #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            if self.sDE2 != '':
                plt.plot(x,y, 'b', label='y='+self.sDE2)
            plt.legend(loc='upper left')
            self.newEquation = self.sDE2
            if '/' in self.sDE2:
                self.newEquation = self.sDE2.replace('/','')
            plt.savefig('graphs/' + self.newEquation + 'new.png', bbox_inches='tight')
            image2 = Image.open("graphs/" + self.newEquation + "new.png")
            self.graphImage1 = ImageTk.PhotoImage(image2)
        #https://matplotlib.org/tutorials/introductory/pyplot.html

        #950,132,1150,163
        if event.x>950 and event.x<1150 and event.y>132 and event.y<163:
            self.graphP3 = True
            self.submit = False
            x1 =-np.pi
            x2 = np.pi
            x = np.linspace(x1,x2,100)
            self.npEquation = self.sDE3
            if 'sin' in self.sDE3:
                self.npEquation = self.npEquation.replace('sin','np.sin')
            if 'cos' in self.sDE3:
                self.npEquation = self.npEquation.replace('cos','np.cos')
            if 'tan' in self.sDE3:
                self.npEquation = self.npEquation.replace('tan','np.tan')
            if 'exp' in self.sDE3:
                self.npEquation = self.npEquation.replace('exp','np.exp')
            if 'ln' in self.sDE3:
                self.npEquation = self.npEquation.replace('ln','np.log')
            if self.sDE3 != '':
                y = eval(self.npEquation)
            fig = plt.figure(figsize = (4,3))
            ax = fig.add_subplot(1, 1, 1)
            #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            if self.sDE3 != '':
                plt.plot(x,y, 'b', label='y='+self.sDE3)
            plt.legend(loc='upper left')
            self.newEquation = self.sDE3
            if '/' in self.sDE3:
                self.newEquation = self.sDE3.replace('/','')
            plt.savefig('graphs/' + self.newEquation + 'new.png', bbox_inches='tight')
            image2 = Image.open("graphs/" + self.newEquation + "new.png")
            self.graphImage1 = ImageTk.PhotoImage(image2)
        #https://matplotlib.org/tutorials/introductory/pyplot.html
        
        #950,163,1150,194
        if event.x>950 and event.x<1150 and event.y>163 and event.y<194:
            self.graphP4 = True
            self.submit = False
            x1 =-np.pi
            x2 = np.pi
            x = np.linspace(x1,x2,100)
            self.npEquation = self.sDE4
            if 'sin' in self.sDE4:
                self.npEquation = self.npEquation.replace('sin','np.sin')
            if 'cos' in self.sDE4:
                self.npEquation = self.npEquation.replace('cos','np.cos')
            if 'tan' in self.sDE4:
                self.npEquation = self.npEquation.replace('tan','np.tan')
            if 'exp' in self.sDE4:
                self.npEquation = self.npEquation.replace('exp','np.exp')
            if 'ln' in self.sDE4:
                self.npEquation = self.npEquation.replace('ln','np.log')
            if self.sDE4 != '':
                y = eval(self.npEquation)
            fig = plt.figure(figsize = (4,3))
            ax = fig.add_subplot(1, 1, 1)
            #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            if self.sDE4 != '':
                plt.plot(x,y, 'b', label='y='+self.sDE4)
            plt.legend(loc='upper left')
            self.newEquation = self.sDE4
            if '/' in self.sDE4:
                self.newEquation = self.sDE4.replace('/','')
            plt.savefig('graphs/' + self.newEquation + 'new.png', bbox_inches='tight')
            image2 = Image.open("graphs/" + self.newEquation + "new.png")
            self.graphImage1 = ImageTk.PhotoImage(image2)
        #https://matplotlib.org/tutorials/introductory/pyplot.html
    
    #950,194,1150,225
        if event.x>950 and event.x<1150 and event.y>194 and event.y<225:
            self.graphP5 = True
            self.submit = False
            x1 =-np.pi
            x2 = np.pi
            x = np.linspace(x1,x2,100)
            self.npEquation = self.sDE5
            if 'sin' in self.sDE5:
                self.npEquation = self.npEquation.replace('sin','np.sin')
            if 'cos' in self.sDE5:
                self.npEquation = self.npEquation.replace('cos','np.cos')
            if 'tan' in self.sDE5:
                self.npEquation = self.npEquation.replace('tan','np.tan')
            if 'exp' in self.sDE5:
                self.npEquation = self.npEquation.replace('exp','np.exp')
            if 'ln' in self.sDE5:
                self.npEquation = self.npEquation.replace('ln','np.log')
            if self.sDE5 != '':
                y = eval(self.npEquation)
            fig = plt.figure(figsize = (4,3))
            ax = fig.add_subplot(1, 1, 1)
            #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            if self.sDE4 != '':
                plt.plot(x,y, 'b', label='y='+self.sDE5)
            plt.legend(loc='upper left')
            self.newEquation = self.sDE5
            if '/' in self.sDE5:
                self.newEquation = self.sDE4.replace('/','')
            plt.savefig('graphs/' + self.newEquation + 'new.png', bbox_inches='tight')
            image2 = Image.open("graphs/" + self.newEquation + "new.png")
            self.graphImage1 = ImageTk.PhotoImage(image2)
        #https://matplotlib.org/tutorials/introductory/pyplot.html


    #950,225,1150,256
        if event.x>950 and event.x<1150 and event.y>225 and event.y<256:
            self.graphP6 = True
            self.submit = False
            x1 =-np.pi
            x2 = np.pi
            x = np.linspace(x1,x2,100)
            self.npEquation = self.sDE6
            if 'sin' in self.sDE6:
                self.npEquation = self.npEquation.replace('sin','np.sin')
            if 'cos' in self.sDE6:
                self.npEquation = self.npEquation.replace('cos','np.cos')
            if 'tan' in self.sDE6:
                self.npEquation = self.npEquation.replace('tan','np.tan')
            if 'exp' in self.sDE6:
                self.npEquation = self.npEquation.replace('exp','np.exp')
            if 'ln' in self.sDE6:
                self.npEquation = self.npEquation.replace('ln','np.log')
            if self.sDE6 != '':
                y = eval(self.npEquation)
            fig = plt.figure(figsize = (4,3))
            ax = fig.add_subplot(1, 1, 1)
            #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            if self.sDE6 != '':
                plt.plot(x,y, 'b', label='y='+self.sDE6)
            plt.legend(loc='upper left')
            self.newEquation = self.sDE6
            if '/' in self.sDE6:
                self.newEquation = self.sDE6.replace('/','')
            plt.savefig('graphs/' + self.newEquation + 'new.png', bbox_inches='tight')
            image2 = Image.open("graphs/" + self.newEquation + "new.png")
            self.graphImage1 = ImageTk.PhotoImage(image2)
        #https://matplotlib.org/tutorials/introductory/pyplot.html


    #950,256,1150,287
        if event.x>950 and event.x<1150 and event.y>256 and event.y<287:
            self.graphP7 = True
            self.submit = False
            x1 =-np.pi
            x2 = np.pi
            x = np.linspace(x1,x2,100)
            self.npEquation = self.sDE7
            if 'sin' in self.sDE7:
                self.npEquation = self.npEquation.replace('sin','np.sin')
            if 'cos' in self.sDE7:
                self.npEquation = self.npEquation.replace('cos','np.cos')
            if 'tan' in self.sDE7:
                self.npEquation = self.npEquation.replace('tan','np.tan')
            if 'exp' in self.sDE7:
                self.npEquation = self.npEquation.replace('exp','np.exp')
            if 'ln' in self.sDE7:
                self.npEquation = self.npEquation.replace('ln','np.log')
            if self.sDE7 != '':
                y = eval(self.npEquation)
            fig = plt.figure(figsize = (4,3))
            ax = fig.add_subplot(1, 1, 1)
            #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            if self.sDE7 != '':
                plt.plot(x,y, 'b', label='y='+self.sDE7)
            plt.legend(loc='upper left')
            self.newEquation = self.sDE7
            if '/' in self.sDE7:
                self.newEquation = self.sDE7.replace('/','')
            plt.savefig('graphs/' + self.newEquation + 'new.png', bbox_inches='tight')
            image2 = Image.open("graphs/" + self.newEquation + "new.png")
            self.graphImage1 = ImageTk.PhotoImage(image2)
        #https://matplotlib.org/tutorials/introductory/pyplot.html

        #950,287,1150,318
        if event.x>950 and event.x<1150 and event.y>287 and event.y<318:
            self.graphP8 = True
            self.submit = False
            x1 =-np.pi
            x2 = np.pi
            x = np.linspace(x1,x2,100)
            self.npEquation = self.sDE8
            if 'sin' in self.sDE8:
                self.npEquation = self.npEquation.replace('sin','np.sin')
            if 'cos' in self.sDE8:
                self.npEquation = self.npEquation.replace('cos','np.cos')
            if 'tan' in self.sDE8:
                self.npEquation = self.npEquation.replace('tan','np.tan')
            if 'exp' in self.sDE8:
                self.npEquation = self.npEquation.replace('exp','np.exp')
            if 'ln' in self.sDE8:
                self.npEquation = self.npEquation.replace('ln','np.log')
            if self.sDE8 != '':
                y = eval(self.npEquation)
            fig = plt.figure(figsize = (4,3))
            ax = fig.add_subplot(1, 1, 1)
            #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            if self.sDE8 != '':
                plt.plot(x,y, 'b', label='y='+self.sDE8)
            plt.legend(loc='upper left')
            self.newEquation = self.sDE8
            if '/' in self.sDE8:
                self.newEquation = self.sDE8.replace('/','')
            plt.savefig('graphs/' + self.newEquation + 'new.png', bbox_inches='tight')
            image2 = Image.open("graphs/" + self.newEquation + "new.png")
            self.graphImage1 = ImageTk.PhotoImage(image2)
        #https://matplotlib.org/tutorials/introductory/pyplot.html

        #950,318,1150,349
        if event.x>950 and event.x<1150 and event.y>318 and event.y<349:
            self.graphP9 = True
            self.submit = False
            x1 =-np.pi
            x2 = np.pi
            x = np.linspace(x1,x2,100)
            self.npEquation = self.sDE9
            if 'sin' in self.sDE9:
                self.npEquation = self.npEquation.replace('sin','np.sin')
            if 'cos' in self.sDE9:
                self.npEquation = self.npEquation.replace('cos','np.cos')
            if 'tan' in self.sDE9:
                self.npEquation = self.npEquation.replace('tan','np.tan')
            if 'exp' in self.sDE9:
                self.npEquation = self.npEquation.replace('exp','np.exp')
            if 'ln' in self.sDE9:
                self.npEquation = self.npEquation.replace('ln','np.log')
            if self.sDE9 != '':
                y = eval(self.npEquation)
            fig = plt.figure(figsize = (4,3))
            ax = fig.add_subplot(1, 1, 1)
            #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            if self.sDE9 != '':
                plt.plot(x,y, 'b', label='y='+self.sDE7)
            plt.legend(loc='upper left')
            self.newEquation = self.sDE9
            if '/' in self.sDE9:
                self.newEquation = self.sDE9.replace('/','')
            plt.savefig('graphs/' + self.newEquation + 'new.png', bbox_inches='tight')
            image2 = Image.open("graphs/" + self.newEquation + "new.png")
            self.graphImage1 = ImageTk.PhotoImage(image2)
        #https://matplotlib.org/tutorials/introductory/pyplot.html

        #950,349,1150,380
        if event.x>950 and event.x<1150 and event.y>349 and event.y<380:
            self.graphP10 = True
            self.submit = False
            x1 =-np.pi
            x2 = np.pi
            x = np.linspace(x1,x2,100)
            self.npEquation = self.sDE10
            if 'sin' in self.sDE10:
                self.npEquation = self.npEquation.replace('sin','np.sin')
            if 'cos' in self.sDE10:
                self.npEquation = self.npEquation.replace('cos','np.cos')
            if 'tan' in self.sDE10:
                self.npEquation = self.npEquation.replace('tan','np.tan')
            if 'exp' in self.sDE10:
                self.npEquation = self.npEquation.replace('exp','np.exp')
            if 'ln' in self.sDE10:
                self.npEquation = self.npEquation.replace('ln','np.log')
            if self.sDE10 != '':
                y = eval(self.npEquation)
            fig = plt.figure(figsize = (4,3))
            ax = fig.add_subplot(1, 1, 1)
            #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('center')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            if self.sDE10 != '':
                plt.plot(x,y, 'b', label='y='+self.sDE10)
            plt.legend(loc='upper left')
            self.newEquation = self.sDE10
            if '/' in self.sDE10:
                self.newEquation = self.sDE10.replace('/','')
            plt.savefig('graphs/' + self.newEquation + 'new.png', bbox_inches='tight')
            image2 = Image.open("graphs/" + self.newEquation + "new.png")
            self.graphImage1 = ImageTk.PhotoImage(image2)
        #https://matplotlib.org/tutorials/introductory/pyplot.html
    #Show every user input

        if event.x > 200 and event.x <860 and event.y > 354 and event.y <390:
            if len(str(self.secondderivative))>100:
                self.sub = True
            
        if event.x > 200 and event.x < 860 and event.y > 318 and event.y<354:
            if len(str(self.firstderivative))>100:
                self.sub1 = True

        if event.x > 200 and event.x < 860 and event.y > 282 and event.y < 318:
            if len(str(self.derivative))>100:
                self.sub2 = True
            
        if event.x > 170 and event.x < 740 and event.y > 435 and event.y < 480:
            if len(str(self.integral))>70:
                self.subI = True

        if event.x > 140 and event.x < 280 and event.y > 540 and event.y < 580:
            if len(str(self.domain))>18:
                self.subD = True
                
        if event.x > 365 and event.x < 505 and event.y > 540 and event.y < 580:
            if len(str(self.range))>18:
                self.subR = True

        if event.x > 590 and event.x < 730 and event.y > 540 and event.y < 580:
            if len(str(self.roots))>18:
                self.subRo = True

        if event.x > 150 and event.x <650 and event.y > 640 and event.y < 680:
            if len(str(self.asymptotes))>70:
                self.subA = True

    def solverKeyPressed(self,event):
        if self.sub == True:
            if len(str(self.secondderivative)) > 100:
                self.secderivative2 = str(self.secondderivative)[self.xer:self.yer]
            if event.key == 'Right':
                if self.yer != len(str(self.secondderivative)):
                    self.xer += 1
                    self.yer += 1
                    self.secderivative2 = str(self.secondderivative)[self.xer:self.yer]
                if self.yer >= len(str(self.secondderivative)):
                    self.xer += 0
                    self.yer += 0
                    self.secderivative2 = str(self.secondderivative)[self.xer:self.yer]
            if event.key == 'Left':
                if self.xer != 0:
                    self.xer -= 1
                    self.yer -= 1
                    self.secderivative2 = str(self.secondderivative)[self.xer:self.yer]
                if self.xer == 0:
                    self.xer -= 0
                    self.yer -= 0
                    self.secderivative2 = str(self.secondderivative)[self.xer:self.yer]
        if self.sub1 == True:
            if len(str(self.firstderivative)) > 100:
                self.firstderivative2 = str(self.firstderivative)[self.xer1:self.yer1]
            if event.key == 'Right':
                if self.yer != len(str(self.firstderivative)):
                    self.xer1 += 1
                    self.yer1 += 1
                    self.firstderivative2 = str(self.firstderivative)[self.xer1:self.yer1]
                if self.yer1 >= len(str(self.firstderivative)):
                    self.xer1 += 0
                    self.yer1 += 0
                    self.firstderivative2 = str(self.firstderivative)[self.xer1:self.yer1]
            if event.key == 'Left':
                if self.xer != 0:
                    self.xer1 -= 1
                    self.yer1 -= 1
                    self.firstderivative2 = str(self.firstderivative)[self.xer1:self.yer1]
                if self.xer1 == 0:
                    self.xer1 -= 0
                    self.yer1 -= 0
                    self.firstderivative2 = str(self.firstderivative)[self.xer1:self.yer1]
        if self.sub2 == True:
            if len(str(self.derivative)) > 100:
                self.derivative2 = str(self.derivative)[self.xer2:self.yer2]
            if event.key == 'Right':
                if self.yer2 != len(str(self.derivative)):
                    self.xer2 += 1
                    self.yer2 += 1
                    self.derivative2 = str(self.derivative)[self.xer2:self.yer2]
                if self.yer2 >= len(str(self.derivative)):
                    self.xer2 += 0
                    self.yer2 += 0
                    self.derivative2 = str(self.derivative)[self.xer2:self.yer2]
            if event.key == 'Left':
                if self.xer2 != 0:
                    self.xer2 -= 1
                    self.yer2 -= 1
                    self.derivative2 = str(self.derivative)[self.xer2:self.yer2]
                if self.xer2 == 0:
                    self.xer2 -= 0
                    self.yer2 -= 0
                    self.derivative2 = str(self.derivative)[self.xer2:self.yer2]
        if self.subI == True:
            if len(str(self.integral)) > 70:
                self.modIntegral2 = str(self.integral)[self.xerI:self.yerI]
            if event.key == 'Right':
                if self.yerI != len(str(self.integral)):
                    self.xerI += 1
                    self.yerI += 1
                    self.modIntegral2 = str(self.integral)[self.xerI:self.yerI]
                if self.yerI >= len(str(self.integral)):
                    self.xerI += 0
                    self.yerI += 0
                    self.modIntegral2 = str(self.integral)[self.xerI:self.yerI]
            if event.key == 'Left':
                if self.xerI != 0:
                    self.xerI -= 1
                    self.yerI -= 1
                    self.modIntegral2 = str(self.integral)[self.xerI:self.yerI]
                if self.xerI == 0:
                    self.xerI -= 0
                    self.yerI -= 0
                    self.modIntegral2 = str(self.integral)[self.xerI:self.yerI]
        if self.subD == True:
            if len(str(self.domain)) > 18:
                self.modDomain2 = str(self.domain)[self.xerD:self.yerD]
            if event.key == 'Right':
                if self.yerD != len(str(self.domain)):
                    self.xerD += 1
                    self.yerD += 1
                    self.modDomain2 = str(self.domain)[self.xerD:self.yerD]
                if self.yerD >= len(str(self.domain)):
                    self.xerD += 0
                    self.yerD += 0
                    self.modDomain2 = str(self.domain)[self.xerD:self.yerD]
            if event.key == 'Left':
                if self.xerD != 0:
                    self.xerD -= 1
                    self.yerD -= 1
                    self.modDomain2 = str(self.domain)[self.xerD:self.yerD]
                if self.xerD == 0:
                    self.xerD -= 0
                    self.yerD -= 0
                    self.modDomain2 = str(self.domain)[self.xerD:self.yerD]
        if self.subR == True:
            if len(str(self.range)) > 18:
                self.modRange2 = str(self.range)[self.xerR:self.yerR]
            if event.key == 'Right':
                if self.yerR != len(str(self.range)):
                    self.xerR += 1
                    self.yerR += 1
                    self.modRange2 = str(self.range)[self.xerR:self.yerR]
                if self.yerR >= len(str(self.range)):
                    self.xerR += 0
                    self.yerR += 0
                    self.modRange2 = str(self.range)[self.xerR:self.yerR]
            if event.key == 'Left':
                if self.xerR != 0:
                    self.xerR -= 1
                    self.yerR -= 1
                    self.modRange2 = str(self.range)[self.xerR:self.yerR]
                if self.xerR == 0:
                    self.xerR -= 0
                    self.yerR -= 0
                    self.modRange2 = str(self.range)[self.xerR:self.yerR]
        if self.subRo == True:
            if len(str(self.roots)) > 18:
                self.modRoots2 = str(self.roots)[self.xerRo:self.yerRo]
            if event.key == 'Right':
                if self.yerRo != len(str(self.roots)):
                    self.xerRo += 1
                    self.yerRo += 1
                    self.modRoots2 = str(self.roots)[self.xerRo:self.yerRo]
                if self.yerRo >= len(str(self.roots)):
                    self.xerRo += 0
                    self.yerRo += 0
                    self.modRoots2 = str(self.roots)[self.xerRo:self.yerRo]
            if event.key == 'Left':
                if self.xerRo != 0:
                    self.xerRo -= 1
                    self.yerRo -= 1
                    self.modRoots2 = str(self.roots)[self.xerRo:self.yerRo]
                if self.xerRo == 0:
                    self.xerRo -= 0
                    self.yerRo -= 0
                    self.modRoots2 = str(self.roots)[self.xerRo:self.yerRo]
        if self.subA == True:
            if len(str(self.asymptotes)) > 70:
                self.modAsy2 = str(self.asymptotes)[self.xerA:self.yerA]
            if event.key == 'Right':
                if self.yerA != len(str(self.asymptotes)):
                    self.xerA += 1
                    self.yerA += 1
                    self.modAsy2 = str(self.asymptotes)[self.xerA:self.yerA]
                if self.yerA >= len(str(self.asymptotes)):
                    self.xerA += 0
                    self.yerA += 0
                    self.modAsy2 = str(self.asymptotes)[self.xerA:self.yerA]
            if event.key == 'Left':
                if self.xerA != 0:
                    self.xerA -= 1
                    self.yerA -= 1
                    self.modAsy2 = str(self.asymptotes)[self.xerA:self.yerA]
                if self.xerA == 0:
                    self.xerA -= 0
                    self.yerA -= 0
                    self.modAsy2 = str(self.asymptotes)[self.xerA:self.yerA]

    def solverRedrawAll(self,canvas):
        canvas.create_rectangle(0,0,self.width,self.height, fill ="#b2cecf",width = 0)
        canvas.create_text(600,200, text = 'An Easy Math Solver', font = 'Arial 28 bold')
        canvas.create_image(600,20, image=self.homeImage, anchor =N)
        canvas.create_rectangle(40,30,180,100,fill = "#0e385f",outline ='white')
        canvas.create_text(110,65,text = "Home", fill = 'white', font = 'Arial 28 bold')

        #Derivative 
        canvas.create_line(100, 250, 900, 250, fill="black", width = 3)
        canvas.create_text(180, 270, text = 'Derivatives:', fill = 'Black', font = 'Arial 24 bold')
        canvas.create_rectangle(200,282,860,318,fill = '#b2cecf', outline = '#0e385f')
        if self.sub2 == False and self.lensub == False:
            canvas.create_text(540,300, text = self.derivative, fill = '#0e385f', font = 'Arial 16')
        if self.lensub == True and self.sub2 == False:   
            canvas.create_text(540,300, text = self.derivative1, fill = '#0e385f', font = 'Arial 16')
        if self.sub2 == True:   
            canvas.create_text(540,300, text = self.derivative2, fill = '#0e385f', font = 'Arial 16')
        canvas.create_text(180,300, text = '1)', fill = '#0e385f', font = 'Arial 18 bold')
        canvas.create_rectangle(200,318,860,354,fill = '#b2cecf', outline = '#0e385f')
        if self.sub1 == False and self.lensub1 == False:
            canvas.create_text(540,336, text = self.firstderivative, fill = '#0e385f', font = 'Arial 16')
        if self.lensub1 == True and self.sub1 == False:   
            canvas.create_text(540,336, text = self.firstderivative1, fill = '#0e385f', font = 'Arial 16')
        if self.sub1 == True:   
            canvas.create_text(540,336, text = self.firstderivative2, fill = '#0e385f', font = 'Arial 16')
        canvas.create_text(180,336, text = '2)', fill = '#0e385f', font = 'Arial 18 bold')
        canvas.create_rectangle(200,354,860,390,fill = '#b2cecf', outline = '#0e385f')
        if self.sub == False and self.lensub2 == False:
            canvas.create_text(540,372, text = self.secondderivative, fill = '#0e385f', font = 'Arial 16')
        if self.lensub2 == True and self.sub == False:
            canvas.create_text(540,372, text = self.secderivative1, fill = '#0e385f', font = 'Arial 16')
        if self.sub == True:
            canvas.create_text(540,372, text = self.secderivative2, fill = '#0e385f', font = 'Arial 16')
        canvas.create_text(180,372, text = '3)', fill = '#0e385f', font = 'Arial 18 bold')

        #Integral
        canvas.create_line(100,400,900,400, fill = 'black', width = 3)
        canvas.create_text(170, 420, text = 'Integral:', fill = 'Black', font = 'Arial 24 bold')
        canvas.create_rectangle(170,435,740,480, fill = '#b2cecf', outline = '#0e385f') 
        if self.subI == False and self.lensubI == False:
            canvas.create_text(455,460, text = self.integral, font = 'Arial 16', fill = '#0e385f')
        if self.lensubI == True and self.subI == False:
            canvas.create_text(455,460, text = self.modIntegral1, font = 'Arial 16', fill = '#0e385f')
        if self.subI == True:
            canvas.create_text(455,460, text = self.modIntegral2, font = 'Arial 16', fill = '#0e385f')

        #Domain/Range/Roots
        canvas.create_line(100,500,750,500, fill = 'black', width = 3)
        canvas.create_text(210, 520, text = 'Domain:', fill = 'Black', font = 'Arial 24 bold')
        canvas.create_text(435, 520, text = 'Range:', fill = 'Black', font = 'Arial 24 bold')
        canvas.create_text(660, 520, text = 'Roots:', fill = 'Black', font = 'Arial 24 bold')
        canvas.create_line(320,500,320,600, fill = 'black', width = 1)
        canvas.create_line(560,500,560,600, fill = 'black', width = 1)
        canvas.create_rectangle(120,540,300,580, fill = '#b2cecf', outline = '#0e385f')
        if self.subD == False and self.lensubD == False:
            canvas.create_text(210, 560, text = self.domain, fill = '#0e385f', font = 'Arial 16')
        if self.lensubD == True and self.subD == False:
            canvas.create_text(210, 560, text = self.modDomain1, fill = '#0e385f', font = 'Arial 16')
        if self.subD == True:
            canvas.create_text(210, 560, text = self.modDomain2, fill = '#0e385f', font = 'Arial 16')
        canvas.create_rectangle(365,540,505,580, fill = '#b2cecf', outline = '#0e385f')
        if self.subR == False and self.lensubR == False:
            canvas.create_text(435, 560, text = self.range, fill = '#0e385f', font = 'Arial 16')
        if self.lensubR == True and self.subR == False:
            canvas.create_text(435, 560, text = self.modRange1, fill = '#0e385f', font = 'Arial 16')
        if self.subR == True:
            canvas.create_text(435, 560, text = self.modRange2, fill = '#0e385f', font = 'Arial 16')
        canvas.create_rectangle(590,540,730,580,fill = '#b2cecf', outline = '#0e385f' )
        if self.subRo == False and self.lensubRo == False:
            canvas.create_text(660, 560, text = self.roots, fill = '#0e385f', font = 'Arial 16')
        if self.lensubRo == True and self.subRo == False:
            canvas.create_text(660, 560, text = self.modRoots1, fill = '#0e385f', font = 'Arial 16')
        if self.subRo == True:
            canvas.create_text(660, 560, text = self.modRoots2, fill = '#0e385f', font = 'Arial 16')

        #Asymptotes
        canvas.create_line(100,600,750,600, fill = 'black', width = 3)
        canvas.create_text(190, 620, text = 'Asymptotes:', fill = 'Black', font = 'Arial 24 bold')
        canvas.create_rectangle(150,640,650,680,fill = '#b2cecf', outline = '#0e385f')
        if self.subA == False and self.lensubA == False:
            canvas.create_text(400,660, text = self.asymptotes, fill = '#0e385f', font = 'Arial 16')
        if self.lensubA == True and self.subA == False:
            canvas.create_text(400,660, text = self.modAsy1, fill = '#0e385f', font = 'Arial 16')
        if self.subA == True:
            canvas.create_text(400,660, text = self.modAsy2, fill = '#0e385f', font = 'Arial 16')

        #New Equation/User Button
        canvas.create_line(100,700,750,700, fill = 'black', width = 3)
        canvas.create_rectangle(200,720,500,790, fill = '#0e385f', outline = 'white')
        canvas.create_text(350,750, text = 'Enter New Equation/User', fill = 'white', font = 'Arial 24 bold')

        #Graph Screen
        if self.submit == True:
            canvas.create_image(990,480, image = self.graphImage, anchor = N)
        elif self.graphP1 == True:
            canvas.create_image(990,480, image = self.graphImage1, anchor = N)
        elif self.graphP2 == True:
            canvas.create_image(990,480, image = self.graphImage1, anchor = N)
        elif self.graphP3 == True:
            canvas.create_image(990,480, image = self.graphImage1, anchor = N)
        elif self.graphP4 == True:
            canvas.create_image(990,480, image = self.graphImage1, anchor = N)
        elif self.graphP5 == True:
            canvas.create_image(990,480, image = self.graphImage1, anchor = N)
        elif self.graphP6 == True:
            canvas.create_image(990,480, image = self.graphImage1, anchor = N)
        elif self.graphP7 == True:
            canvas.create_image(990,480, image = self.graphImage1, anchor = N)
        elif self.graphP8 == True:
            canvas.create_image(990,480, image = self.graphImage1, anchor = N)
        elif self.graphP9 == True:
            canvas.create_image(990,480, image = self.graphImage1, anchor = N)
        elif self.graphP10 == True:
            canvas.create_image(990,480, image = self.graphImage1, anchor = N)
        elif self.submit == False and self.graphP1 == False:
            canvas.create_rectangle(810,460,1150,730, fill = '#b2cecf', outline = '#0e385f' )
        canvas.create_text(980,450, text = 'Graph', fill = 'black', font = 'Arial 24 bold')
        canvas.create_rectangle(900,740,1050,780, fill = '#0e385f', outline = 'white')
        canvas.create_text(975,760, text = 'Detailed Graph', fill = 'white', font = 'Arial 18 bold')

        #Previous Equations
        canvas.create_rectangle(950,70,1150,101, fill = '#b2cecf', outline = '#0e385f')
        canvas.create_text(1050,93, text = self.sDE1, fill = '#0e385f', font = 'Arial 16')
        canvas.create_rectangle(950,101,1150,132, fill = '#b2cecf', outline = '#0e385f')
        canvas.create_text(1050,124, text = self.sDE2, fill = '#0e385f', font = 'Arial 16')
        canvas.create_rectangle(950,132,1150,163, fill = '#b2cecf', outline = '#0e385f')
        canvas.create_text(1050,155, text = self.sDE3, fill = '#0e385f', font = 'Arial 16')
        canvas.create_rectangle(950,163,1150,194, fill = '#b2cecf', outline = '#0e385f')
        canvas.create_text(1050,186, text = self.sDE4, fill = '#0e385f', font = 'Arial 16')
        canvas.create_rectangle(950,194,1150,225, fill = '#b2cecf', outline = '#0e385f')
        canvas.create_text(1050,217, text = self.sDE5, fill = '#0e385f', font = 'Arial 16')
        canvas.create_rectangle(950,225,1150,256, fill = '#b2cecf', outline = '#0e385f')
        canvas.create_text(1050,249, text = self.sDE6, fill = '#0e385f', font = 'Arial 16')
        canvas.create_rectangle(950,256,1150,287, fill = '#b2cecf', outline = '#0e385f')
        canvas.create_text(1050,279, text = self.sDE7, fill = '#0e385f', font = 'Arial 16')
        canvas.create_rectangle(950,287,1150,318, fill = '#b2cecf', outline = '#0e385f')
        canvas.create_text(1050,311, text = self.sDE8, fill = '#0e385f', font = 'Arial 16')
        canvas.create_rectangle(950,318,1150,349, fill = '#b2cecf', outline = '#0e385f')
        canvas.create_text(1050,342, text = self.sDE9, fill = '#0e385f', font = 'Arial 16')
        canvas.create_rectangle(950,349,1150,380, fill = '#b2cecf', outline = '#0e385f')
        canvas.create_text(1050,372, text = self.sDE10, fill = '#0e385f', font = 'Arial 16')
        canvas.create_text(1050,50, text = 'Previous Equations:', fill = 'black', font = 'Arial 20 bold')
        #canvas.create_text(1050,225, text = self.storeDEquation, fill = '#0e385f', font = 'Arial 16')

#Graph Menu

    def graphMousePressed(self,event):
        mouseX = event.x
        mouseY = event.y
    
        #Home Button
        if event.x > 40 and event.x < 180 and event.y > 30 and event.y < 100:
            self.currentState = self.differStates[0]

        #Solver Button
        if event.x > 40 and event.x < 180 and event.y > 120 and event.y < 190:
            self.currentState = self.differStates[1]

    def graphRedrawAll(self,canvas):
        canvas.create_rectangle(0,0,self.width,self.height, fill ="#b2cecf",width = 0)
        canvas.create_text(600,200, text = 'An Easy Math Solver', font = 'Arial 28 bold')
        canvas.create_image(600,20, image=self.homeImage, anchor =N)
        canvas.create_rectangle(40,30,180,100,fill = "#0e385f",outline ='white')
        canvas.create_text(110,65,text = "Home", fill = 'white', font = 'Arial 28 bold')
        canvas.create_rectangle(40,120,180,190,fill = "#0e385f",outline ='white')
        canvas.create_text(110,155,text = "Solver", fill = 'white', font = 'Arial 28 bold')
        if self.submit == True:
            canvas.create_image(600,250, image = self.newgraphImage, anchor = N)
        else:
            canvas.create_rectangle(180,260,1050,750, fill = '#b2cecf', outline = '#0e385f')


Display(width = 1200, height = 1200)

