## @file CurveADT.py
#  @author Stephanus Jonatan
#  @date January 21, 2018

from SeqADT import SeqT
from numpy import *

## @brief CurveT is a class that analyzes data of a polynomial.
#  @details CurveT uses interpolation and regression to estimate a y value for a given x value.
#  @details CurveT uses imported classes SeqT and the numpy library.
class CurveT(object):
    ## @brief Initializes two empty sequences that stores x and y coordinates from a .txt file.
    #  @details reads a .txt file with data of a polynomial and stores each x and y coordinate sequentially in their own respective lists.
    def __init__(self, s):
        # Initializes two empty sequences
        self.Points_x = SeqT()
        self.Points_y = SeqT()
        # Reads file "s" that contains data points (e.g. x, y) separated by a
        # comma and a space, and with each point on a newline.
        Seq_file = open(s, 'r')
        lines = Seq_file.readlines()
        # Reads each line one at a time, and stores it in i
        for i in lines:
            # Strips all new line characters in the line, and stores it back into i
            i = i.strip()
            # Splits a string at every occurring comma into elements, and
            # adds it to a list, add_point.
            add_point = i.split(",")
            # Adds add_point[0] and add_point[1] into lists Points_x
            # and Points_y respectively as an int data type.
            self.Points_x.add(self.Points_x.size(), float(add_point[0]))
            self.Points_y.add(self.Points_y.size(), float(add_point[1]))

    ## @brief linVal(x) calculates the approximate y value of a given x value using linear interpolation.
    #  @param x is the given value.
    def linVal(self, x):
        # finds approximate position (i) of value x in sequence Points_x
        # (either the exact position, or the position to the left of it)
        i = self.Points_x.indexInSeq(x)
        # finds the x and y value at the ith position
        x1 = self.Points_x.Seq[i]
        y1 = self.Points_y.Seq[i]
        # finds the x and y values at the position to the right of i
        x2 = self.Points_x.Seq[i + 1]
        y2 = self.Points_y.Seq[i + 1]

        # linear interpolation formula
        y = ((y2 - y1) / (x2 - x1)) * (x - x1) + y1
        return y

    ## @brief quadVal(x) calculates the approximate y value of a given x value using quadratic interpolation.
    #  @param x is the given value.
    def quadVal(self, x):
        # finds approximate position (i) of value x in sequence Points_x
        # (either the exact position, or the position to the left of it)
        i = self.Points_x.indexInSeq(x)
        # finds the x and y values at the position to the left of i
        x0 = self.Points_x.Seq[i - 1]
        y0 = self.Points_y.Seq[i - 1]

        # finds the x and y value at the ith position
        x1 = self.Points_x.Seq[i]
        y1 = self.Points_y.Seq[i]

        # finds the x and y values at the position to the right of i
        x2 = self.Points_x.Seq[i + 1]
        y2 = self.Points_y.Seq[i + 1]

        # quadratic interpolation formula
        y = y1 + ((y2 - y0) / (x2 - x0)) * (x - x1) + \
            ((y2 - 2 * y1 + y0) / (2 * (x2 - x1) ** 2)) * (x - x1) ** 2
        # y = y0 * (((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))) + \
        #     y1 * (((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))) + \
        #     y2 * (((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1)))
        return y

    ## @brief npolyVal(x) calculates the approximate y value of a given x value using regression.
    #  @details Uses a best fit polynomial to approximate the y value.
    #  @param n is the degree of the best fit polynomial.
    #  @param x is the given value.
    def npolyVal(self, n, x):
        # Checks if degree is at least 1 or greater
        if n >= 1:
        # Evaluates the coefficients of a polynomial with data points
        # Points_x and Points_y, with a polynomial degree of n, and stores
        # it in a list, C.
            C = polyfit(self.Points_x.Seq, self.Points_y.Seq, n)
            # Evaluates polynomial coefficients, C, at the value of x
            y = polyval(C, x)
            return y
        # Otherwise print an error message
        else:
            print("Improper Degree. Must have a degree of at least 1 or greater.")
