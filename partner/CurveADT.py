## @file CurveADT.py
#  @author Ji Who Choi
#  @brief Provides the CurveADT class for representing a curve in the Cartesian
#  x-y plane
#  @date 1/21/2018

import SeqADT
import numpy as np
import os
## @brief An ADT that represents a curve
class CurveT:
  ## @brief CurveT constructor
  #  @details Initializes a CurveT object and assumes the input file, s is in
  #  the same directory as the class. Otherwise, an error occurs.
  #  x and y sequence state variables are set to the values of the first and
  #  second column of s.
  #  @param s the name of a text file in string

    def __init__(self,s):
        #Opens the input textfile,s
        theFolder = os.path.dirname(os.path.abspath(__file__))
        theFile = os.path.join(theFolder, s)
        fileread = open(s, "r")
        filelines = fileread.readlines()
        fileread.close()

        index = 0
        self.xValues = SeqADT.SeqT()
        self.yValues = SeqADT.SeqT()
        for line in filelines:
            splitline = line.split(', ')
            #Split the line to obtain x and y value
            self.x = float (splitline[0])
            self.xValues.add(index, self.x)
            splitline[1] = splitline[1].replace("\n","")
            #replace the end of the newline character to ""
            self.y = float (splitline[1])
            self.yValues.add(index,self.y)
            index += 1

  ## @brief Calculates the value of y using linear interpolation between the
  #  values on either side of x
  #  @details Assumes the point on the curve to the left of x is (x1, y1) and
  #  the point to the right of x is (x2, y2)
  #  @param x a real number
  #  @return the value of y
    def linVal(self, x):
        indexX = self.xValues.indexInSeq(x)
        #finds the first index f the sequence in the range
        x1 = self.xValues.get(indexX)
        #obtains the value at the indexX
        x2 = self.xValues.get(indexX + 1)
        y1 = self.yValues.get(indexX)
        y2 = self.yValues.get(indexX + 1)

        y = ((y2 - y1) / (x2 - x1)) * (x - x1) + (y1)
        return y

  ## @brief Calculates the value of y using quadratic interpolation of three
  #  points with corresponding subscripts of 0, 1, and 2
  #  @details Assumes the point on the curve to the left of x is (x1, y1) and
  #  and the point to the left of (x1, x1) is (x0,y0) and the point to the right
  #  of x is (x2, y2)
  #  @param x a real number
  #  @return the value of y
    def quadVal(self, x):
        indexX = self.xValues.indexInSeq(x)
        x1 = self.xValues.get(indexX)
        #obtains the value at the indexX
        x2 = self.xValues.get(indexX + 1)
        y1 = self.yValues.get(indexX)
        y2 = self.yValues.get(indexX + 1)
        x0 = self.xValues.get(indexX - 1)
        y0 = self.yValues.get(indexX-1)

        y = y1 + ((y2-y0)/(x2-x0)) * (x - x1) + (y2 - 2 * y1 + y0)/ (2 * (x2-x1) ** 2) * ((x - x1) ** 2)
        return y

  ## @brief Calculates the approximation of the value of y at x using regression
  #  @details Uses the polyfit function from numpy to find the best fit
  #  polynomial and then is evaluated at x
  #  @param n an integer number that is the degree of the polynomial
  #  @param x a real number
  #  @return the approximation of the value of y at x
    def npolyVal(self, n, x):
        z = np.polyfit(self.xValues.elements, self.yValues.elements, n)
        p = np.poly1d(z)
        return p(x)
